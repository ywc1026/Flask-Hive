

from pymongo import ASCENDING, DESCENDING
from dbmodel.dbbase import BaseModel
from datetime import datetime, timedelta
import time


class CleanMongoDBCache(BaseModel):

    def __init__(self):
        self.maxcount = 950

    # def insert_test(self):
    #     for i in range(10):
    #         date = (datetime.now()+timedelta(days=i)).strftime('%Y-%m-%d')
    #         for j in range(100):
    #             params = {
    #                 'sql': 'select * from fdate={} and i={}'.format(date, str(j)),
    #                 'flushdate': date,
    #                 'flushcount': j,
    #                 'data': {'a': i}
    #             }
    #             self.mongodb_db.buniss.insert_one(params)

    def run_script(self):
        count = self.mongodb_db.buniss.count()
        overcount = count - self.maxcount
        print overcount

        if overcount > 0:
            res_data = self.mongodb_db.buniss.find().sort([('flushdate', ASCENDING), ('flushcount', ASCENDING)]).limit(overcount)
            res_sql_list = [item.get('sql', '') for item in res_data]
            print res_sql_list
            self.mongodb_db.buniss.remove({"sql": {"$in": res_sql_list}})


def run():
    db = CleanMongoDBCache()
    while True:
        time.sleep(60*60*60)
        db.run_script()


if __name__ == '__main__':

    run()
