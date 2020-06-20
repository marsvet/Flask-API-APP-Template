# -*-coding:utf-8-*-
'''
数据库操作相关代码
'''
from app import db


class User:
    def __init__(self):
        db.ping(reconnect=True) # 如果数据库断开连接，自动重连
        self.cursor = db.cursor()

    def __del__(self):
        self.cursor.close()  # 对象销毁时关闭 cursor

    def getUserInfo(self, user_name):
        sql = "select * from users where user_name='%s'" % user_name
        count = self.cursor.execute(sql)  # count 是受影响的行数，通常用来判断 sql 是否执行成功
        data = self.cursor.fetchall()   # 获取所有查出来的数据
        # db.commit()   # 如果是 insert，delete，update 等操作，需要执行这一句，否则数据不会提交到数据库里
        return count, data[0]
