

from flask import Blueprint, jsonify
from common.response import Response


user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/login', methods=['POST'])
def login():

    data = {
        'code': 0,
        'msg': 'success',
        'data': []
    }

    return jsonify(Response.responseJson((Response.SUCCESS, data = data))


@user.route('/logout', methods=['POST'])
def logout():
    data = {
        'code': 0,
        'msg': 'success',
        'data': []
    }
    return jsonify(data)