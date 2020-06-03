# -*-coding:utf-8-*-
#
# 管理员相关路由
#
from flask import request, jsonify
from app.api import api
from app.utils import mySum


@api.route("/sum")
def calcSum():
    a = request.args['a']
    b = request.args['b']
    theSum = mySum(a, b)
    result = {
        'success': True,
        'sum': theSum
    }
    return result
