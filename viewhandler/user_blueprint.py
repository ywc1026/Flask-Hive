

from flask import Blueprint, jsonify

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/login', methods=['POST'])
def login():

    data = {
        'code': 0,
        'msg': 'success',
        'data': []
    }
    return jsonify(data)


@user.route('/logout', methods=['POST'])
def logout():
    data = {
        'code': 0,
        'msg': 'success',
        'data': []
    }
    return jsonify(data)