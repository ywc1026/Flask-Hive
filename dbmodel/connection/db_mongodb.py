

from pymongo import MongoClient


def connection(host='127.0.0.1', port=27017, database=None):

    conn = MongoClient(host=host, port=port)
    mongo = eval('conn.'+database)
    return mongo


if __name__ == '__main__':

    db = connection('192.168.83.134', database='sys')

    print db.test.insert_one({'a': 1})

    print db.test.find_one()