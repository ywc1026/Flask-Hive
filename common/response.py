

class ErrorCode(object):
    SUCCESS = 0
    ERROR = -1


class Response(ErrorCode):

    @classmethod
    def responseJson(cls, code=None, data=None, msg=None):

        error_msg = {
            cls.ERROR: 'Failed',
            cls.SUCCESS: 'Success'
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

