

from pymongo import MongoClient


def connection(host='127.0.0.1', port=27017):

    conn = MongoClient(host=host, port=port)

    return conn


if __name__ == '__main__':

    db = connection('192.168.83.134')

    print db.mytest.name