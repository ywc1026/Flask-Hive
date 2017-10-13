

from dbbase import BaseModel


class UserInfoModel(BaseModel):

    def add_user(self):

        sql = ''
        self.mysql_db.execute_commit(sql)