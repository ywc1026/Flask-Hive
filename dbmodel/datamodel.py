

from dbbase import BaseModel
from sql_tpl import SQL_TPL, SQL_TPL2
from logger import logger
from datetime import datetime


class DataModel(BaseModel):

    def get_data(self, dims=None, args={}):

        sql = SQL_TPL2.get(dims, None)

        if not sql:
            logger.warning('Not Found sql')
            return []

        sql = sql % args

        # mongodb
        params = {
            'sql': sql
        }
        datenow = datetime.now().date().strftime('%Y-%m-%d')
        res = self.mongodb_db.buniss.find_one(params)
        if not res:
            logger.info('get data from mysql')
            # the speed is very slow when manipulate huge data
            data = self.mysql_db.query_list(sql=sql)
            params = {
                'sql': sql,
                'data': data,
                'flushdate': datenow,
                'flushcount': 1
            }
            self.mongodb_db.buniss.insert_one(params)
        else:
            logger.info('get data from mongodb')
            self.mongodb_db.buniss.update(params, {"$set": {"flushdate": datenow}, "$inc": {"flushcount": 1}}, False, True)

            data = res.get('data', [])

        return data

if __name__ == '__main__':

    db = DataModel()

    params = {
        'sdate': '2017-10-15',
        'edate': '2017-10-20'
    }

    print db.get_data(dims='chart1', args=params)
