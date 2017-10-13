

import redis


def Connection(host='192.168.83.134', port=6379):

    pool = redis.ConnectionPool(host=host, port=port)

    redis_tmp = redis.Redis(connection_pool=pool)

    return redis_tmp


if __name__ == '__main__':

    redis_db = Connection(host='192.168.83.134')
    print redis_db.get('test')