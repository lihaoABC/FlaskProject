import redis
import logging
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from logging.handlers import RotatingFileHandler


db = SQLAlchemy()
redis_store = None


def create_app(config_name):
    """工厂函数"""
    app = Flask(__name__)
    app.config.from_object(config_name)
    db.init_app(app)
    global redis_store
    redis_store = redis.StrictRedis(host=config_name.REDIS.HOST, port=config_name.REDIS_POST, decode_responses=True)
    CSRFProtect(app)
    Session(app)

    return app


def set_logs(config_name):
    """添加日志"""
    # 设置日志的记录等级
    logging.basicConfig(level=config_name.LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)