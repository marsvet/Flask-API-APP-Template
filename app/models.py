# -*-coding:utf-8-*-
#
# 操作数据库的代码全部放到这里
# 其他文件要操作数据库时，先从该文件导入某个类，实例化后调用成员函数
#
from app import db


# 操作用户表的类
class User:  # 创建一个类，类中每个方法的第一个参数必须是 self（相当于 this 指针，代表当前类）
    def __init__(self):  # 相当于构造函数
        db.ping(reconnect=True)
        self.cursor = db.cursor()
        # 每次创建 User 对象时创建 cursor。在成员函数中，用 self.xxx = xxx 的方式创建的是成员变量，直接 xxx = xxx 的方式创建的是局部变量

    def __del__(self):  # 相当于析构函数
        self.cursor.close()  # 对象销毁时关闭 cursor

    def getUserInfo(self, user_name):
        sql = "select * from users where user_name='%s'" % user_name
        count = self.cursor.execute(sql)  # count 是受影响的行数，通常用来判断 sql 是否执行成功
        data = self.cursor.fetchall()   # 获取所有查出来的数据
        # db.commit()   # 如果是 insert，delete，update 等操作，需要执行这一句，否则数据不会提交到数据库里
        return count, data[0]
