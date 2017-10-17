

from dbbase import BaseModel
from logger import logger
import json


class UserInfoModel(BaseModel):

    def check_userauth(self, fwork_id=None, fpassword=None):

        if not fwork_id or not fpassword:
            logger.warning("account or password is none.")
            return False

        sql = 'select fcname, fwork_id, fdept_id, flevel_id from userinfo where fwork_id={fwork_id} and fpassword={fpassword}'.format(fwork_id=fwork_id, fpassword=fpassword)
        data = self.mysql_db.query_one_dict(sql)

        return True if data else False

    def get_userinfo(self, fworkid):
        """
            get the information of the user
        :param fworkid:
        :return:
        """
        if not fworkid:
            logger.warning("the workid is None")
            return {}

        redis_key = self.product_redis_key('userinfo', fworkid)

        data = self.redis_db.hgetall(redis_key)

        if not data:
            sql = 'select fcname, fwork_id, fdept_id, flevel_id from userinfo where fwork_id={fworkid}'.format(fworkid=fworkid)
            data = self.mysql_db.query_one_dict(sql)
            if data:
                self.redis_db.hmset(redis_key, data)
                self.redis_db.expire(redis_key, self.redis_time)

        return data

if __name__ == '__main__':

    db = UserInfoModel()

    print db.get_userinfo(fworkid=1)
