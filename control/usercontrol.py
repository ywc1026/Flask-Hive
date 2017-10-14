

from common.response import Response
from dbmodel.userinfomodel import UserInfoModel
from basecontrol import BaseControl


class UserControl(BaseControl):

    def __init__(self, *args, **kwargs):
        super(UserControl, self).__init__(*args, **kwargs)

        self.userinfomodel = UserInfoModel()

    def user_login(self):

        fworkid = self.args.get('fworkid', None)
        fpassword = self.args.get('fpassword', None)

        if not fworkid:
            return Response.responseJson(Response.INPUT_EMPTY, msg='account is None')

        if not fpassword:
            return Response.responseJson(Response.INPUT_EMPTY, msg='password is None')

        res = self.userinfomodel.check_userauth(fwork_id=fworkid, fpassword=fpassword)
        if res:
            self.session['fworkid'] = fworkid
            return Response.responseJson(Response.SUCCESS, msg="success")
        else:
            return Response.responseJson(Response.ERROR, msg='failed')

    def user_logout(self):
        print self.session['fworkid']
        self.session.pop('fworkid', None)
        return Response.responseJson(Response.SUCCESS, msg='logout success')
