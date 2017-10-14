

class ErrorCode(object):
    SUCCESS = 0
    ERROR = -1
    INPUT_EMPTY = 2
    NO_LOGIN = -3


class Response(ErrorCode):

    @classmethod
    def responseJson(cls, code=None, data=None, msg=None):

        error_msg = {
            cls.ERROR: 'Failed',
            cls.SUCCESS: 'Success',
            cls.INPUT_EMPTY: 'account or password is None',
            cls.NO_LOGIN: 'no login'
        }

        if msg is None:
            msg = error_msg.get(code, 'not defined')
        if data is None:
            data = []

        res = {
            'code': code,
            'msg': msg,
            'data': data
        }

        return res

