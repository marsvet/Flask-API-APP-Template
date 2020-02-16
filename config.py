# -*-coding:utf-8-*-
#
# 项目配置文件
#
import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "hard to guess string."
    JSON_AS_ASCII = False

    pymysql_config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'db': 'database_name',
        'password': os.environ.get('MYSQL_PASSWORD') or 'your db password'
        # flask 首先会去环境变量中获取数据库密码，也就是说，如果通过 `set MYSQL_PASSWORD=xxx` 的方式设置了该环境变量，
        # xxx 会被作为数据库密码，否则 "your db password" 会被作为数据库密码。这样做的目的是防止密码以明文存储在代码中，
        # 开发时可以在代码中明文设置密码，但项目开始正式使用后最好使用环境变量的方式。
    }

    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'xxx@163.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SUBJECT_PREFIX = ''
    MAIL_SENDER = ''
