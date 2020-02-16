# -*-coding:utf-8-*-
#
# 用户相关路由
#
from flask import request, jsonify
from app.models import User
from app.api import api


@api.route("/user_info", methods=["GET"])  # 最后生成的路由会自动变成 "/api/user_info"
def getUserInfo():
    user_name = request.args['user_name']  # 以这种方式获取 GET 方式发送的数据
    # request.json['key']   # POST 方式发送的数据以这种方式获取
    # request.file['key']   # 以这种方式获取文件
    user = User()
    count, data = user.getUserInfo(user_name)
    if count == 0:
        return jsonify({
            'success': False,
            'msg': '找不到此用户'
        })
    else:
        return jsonify({
            'success': True,
            'user_info': data
        })
