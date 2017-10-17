

from dbbase import BaseModel
from logger import logger


class AuthTableModel(BaseModel):

    def get_dims_levelinfo(self, dimsname=None):

        if not dimsname:
            logger.warning('input dimsname is None')
            return {}

        sql = "select fdimsname, flevel_id from authtable where fdimsname='{fdimsname}'".format(fdimsname=dimsname)

        return self.mysql_db.query_one_dict(sql)
