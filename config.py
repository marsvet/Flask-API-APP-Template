# -*-coding:utf-8-*-
'''
项目配置文件
'''
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
        'password': os.environ.get('MYSQL_PASSWORD') or 'db password'
    }

    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'xxx@163.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SUBJECT_PREFIX = ''
    MAIL_SENDER = ''
