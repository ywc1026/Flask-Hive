

from pymysql.cursors import DictCursor
from logger import logger
import pymysql


class Connection(object):

    def __init__(self, host, port=3306, database=None, user=None, password=None, charset='utf8'):

        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.charset = charset

    def execute_commit(self, sql=None):
        try:
            conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.database, charset=self.charset, cursorclass=DictCursor)
            logger.info('sql - {}'.format(sql))

            with conn.cursor() as cursor:
                cursor.execute(sql)
            conn.commit()
            conn.close()
            return True

        except Exception as e:
            logger.error("SQL execute error...{}".format(e))
            conn.rollback()
            conn.close()
            return False

    def execute_query(self, sql=None):
        try:
            conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.database, charset=self.charset, cursorclass=DictCursor)
            logger.info('sql - {}'.format(sql))

            with conn.cursor() as cursor:
                cursor.execute(sql)
                data_list = cursor.fetchall()
            logger.info('sql data -- {}'.format(data_list))
            conn.close()
            return data_list

        except Exception as e:
            logger.error("SQL execute error...{}".format(e))
            conn.rollback()
            conn.close()
            return []

if __name__ == "__main__":

    db = Connection(host='192.168.83.134', port=3306, user='root', password='123', database='system')

    sql = 'select * from userinfo'

    db.execute_query(sql=sql)

    sql = "insert into authtable (ftablename, flevel_id) values ('flask_table', 2)"

    print db.execute_commit(sql=sql)
