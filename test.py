
from dbmodel.dbbase import BaseModel
import datetime


def insert_test_data():

    db = BaseModel()

    insert_sql = 'insert into gameactive (fdate, fuserid, fgameid) values'
    sql_list = []
    for j in range(1, 10):
        fdate = datetime.datetime.now().date().strftime('%Y-%m-%d')
        for i in range(1, 1000):
            sql = "('{}', {}, {})".format(fdate, i+1000, i)
            sql_list.append(sql)

    sql_temp = ','.join(sql_list)
    insert_sql += sql_temp

    print db.mysql_db.execute_commit(insert_sql)


if __name__ == '__main__':
    insert_test_data()