# -*-coding:utf-8-*-
'''
用户相关路由
'''
from flask import request, jsonify
from app.models import User
from app.api import api


@api.route("/user_info", methods=["GET"])
def getUserInfo():
    user_name = request.args['user_name']  # 获取 GET 方式请求时携带的 params
    # request.json['key']   # 获取 POST 方式请求时携带的 JSON 数据
    # request.file['key']   # 获取文件
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
