

from pymongo import ASCENDING, DESCENDING
from dbmodel.dbbase import BaseModel
from datetime import datetime


class CleanMongoDBCache(BaseModel):

    def __init__(self):
        self.maxcount = 100



    def run_script(self):
        count = self.mongodb_db.buniss.count()
        overcount = count - self.maxcount

        if overcount > 0:
            res_data = self.mongodb_db.buniss.find().sort([('flushdate', ASCENDING), ('flushcount', ASCENDING)]).limit(overcount)
            res_sql_list = [item.get('sql', '') for item in res_data]
            self.mongodb_db.buniss.remove({"sql": {"$in": res_sql_list}})


if __name__ == '__main__':

    db = CleanMongoDBCache()

    db.run_script()