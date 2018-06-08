from info import redis_store, constants
from info.modules.passport import passport_blue
from flask import render_template, current_app, request, jsonify, make_response
from info.utils.captcha.captcha import captcha
from info.utils.response_code import RET


@passport_blue.route('/image_code')
def get_image_code():
    """获取图片验证码"""
    # 1. 获取前端生成图片验证码id
    code_id = request.args.get("code_id")
    # 2. 调用工具生成图片验证码
    name, text, image = captcha.generate_captcha()
    # 3. 保存图片内容到redis数据库
    try:
        redis_store.set("imageCodeId_" + code_id, text, constants.IMAGE_CODE_REDIS_EXPIRES)
    except Exception as e:
        current_app.logger.error(e)
        return make_response(jsonify(errno=RET.DBERR, errmsg="保存图片验证码失败"))

    # 4.返回数据
    response = make_response(image)
    response.headers['Content-Type'] = 'image/jpg'
    return response


