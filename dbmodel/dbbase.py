

from connection import db_mongodb, db_redis, db_mysql
import config


class BaseModel(object):

    redis_db = db_redis.connection(host=config.REDIS_HOST, port=config.REDIS_PORT)
    mongodb_db = db_mongodb.connection(host=config.MONGODB_HOST, port=config.MONGODB_PORT)
    mysql_db = db_mysql.Connection(host=config.MYSQL_HOST, port=config.MYSQL_PORT, user=config.MYSQL_USER, password=config.MYSQL_PASSWORD, database=config.MYSQL_DATABASE)

    def __init__(self):

        self.redis_time = 60*60*24
        self.redis_key_prefix = 'yu_'

    def product_redis_key(self, prefix, id):

        redis_key = self.redis_key_prefix+str(prefix)+str(id)
        return redis_key

