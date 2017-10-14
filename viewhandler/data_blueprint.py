# coding=utf-8
from flask import Blueprint, jsonify
from common.auth import auth
from common.response import Response


data = Blueprint('data', __name__, url_prefix='/data')


@data.route('/get_data', methods=['GET'])
@auth.login_require
def get_data():

    option = {
        'title': 'ECharts 入门示例',
        'xAxis': ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
        'series': [{
            'name': '销量',
            'type': 'bar',
            'data': [5, 20, 36, 10, 10, 20]
        }]
    }

    return jsonify(Response.responseJson(Response.SUCCESS, data=option, msg='success'))