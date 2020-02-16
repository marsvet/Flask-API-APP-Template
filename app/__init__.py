from flask import Flask
from config import Config
from pymysql import connect
from flask_mail import Mail

config = Config()
db = connect(**config.pymysql_config)   # 连接数据库
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    mail.init_app(app)

    from app.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app
