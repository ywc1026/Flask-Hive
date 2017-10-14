

from dbbase import BaseModel
from logger import logger


class UserInfoModel(BaseModel):

    def check_userauth(self, fwork_id=None, fpassword=None):

        if not fwork_id or not fpassword:
            logger.warning("account or password is none.")
            return False

        sql = 'select * from userinfo where fwork_id={fwork_id} and fpassword={fpassword}'.format(fwork_id=fwork_id, fpassword=fpassword)
        data = self.mysql_db.query_one_dict(sql)
        return True if data else False
