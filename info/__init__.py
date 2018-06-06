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


