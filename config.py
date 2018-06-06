import logging

import redis


class Config(object):
    """working config"""

    # 密钥
    SECRET_KEY = 'cjfCZ2FT7/ROFRBkV95qup9hspojKEXFxWy/lC+lms0='

    # 默认日志记录等级
    LOG_LEVEL = logging.DEBUG

    # SQLAlchemy数据库配置信息
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/com_2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis缓存数据库配置信息
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # session同步redis配置
    SESSION_TYPE = 'redis'
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 86400
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)


class DevelopmentConfig(Config):
    """ 开发者模式"""
    DEBUG = True


class ProductionConfig(Config):
    """产品上线模式"""
    LOG_LEVEL = logging.ERROR
