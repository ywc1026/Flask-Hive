
from flask import session, jsonify
from common.response import Response


class Auth():

    def login_require(self, func):

        def wrap(*args, **kwargs):

            isLogin = True if session.get('fworkid', None) else False
            if not isLogin:
                return jsonify(Response.NO_LOGIN)

            return func(*args, **kwargs)

        return wrap

auth = Auth()
