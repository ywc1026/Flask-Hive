

from pymongo import ASCENDING, DESCENDING
from dbmodel.dbbase import BaseModel
from datetime import datetime, timedelta


class CleanMongoDBCache(BaseModel):

    def __init__(self):
        self.maxcount = 100

    def insert_test(self):
        for i in range(10):
            date = (datetime.now()+timedelta(days=i)).strftime('%Y-%m-%d')
            for j in range(100):
                params = {
                    'sql': 'select * from fdate={} and i={}'.format(date, str(i)),
                    'flushdate': date,
                    'flushcount': j,
                    'data': {'a': i}
                }
                self.mongodb_db.buniss.insert_one(params)

    def run_script(self):
        count = self.mongodb_db.buniss.count()
        overcount = count - self.maxcount

        if overcount > 0:
            res_data = self.mongodb_db.buniss.find().sort([('flushdate', ASCENDING), ('flushcount', ASCENDING)]).limit(overcount)
            res_sql_list = [item.get('sql', '') for item in res_data]
            self.mongodb_db.buniss.remove({"sql": {"$in": res_sql_list}})


if __name__ == '__main__':

    db = CleanMongoDBCache()

    db.insert_test()