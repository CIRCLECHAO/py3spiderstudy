import random, redis
from cookiespool.config import *


class RedisClient(object):
    def __init__(self, type, website, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        :param type: 类型
        :param website: 网站
        :param host: redis主机
        :param port: redis端口
        :param password: 密码
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password)
        self.type = type
        self.website = website

    def name(self):
        """
        获取hash的名字
        :return:hash名字
        """
        return "{type}:{website}".format(type=self.type, website=self.website)

    def set(self, username, value):
        """
        设置键值对
        :param username:用户名
        :param value:密码或cookies
        :return:
        """
        return self.db.hset(self.name(), username, value)

    def get(self, username):
        """
        根据键名获取键值
        :param username: 键名
        :return:键值
        """
        return self.db.hget(self.name(), username)

    def delete(self, username):
        """
        根据键名删除键值对
        :param username: 键名
        :return:删除结果
        """
        return self.db.hdel(self.name(), username)

    def count(self):
        """
        统计数量
        :return:
        """
        return self.db.hlen(self.name())

    def random(self):
        """
        随机获取键值
        :return:
        """
        return random.choice(self.db.hvals(self.name()))

    def usernames(self):
        """
        获取所有的键值
        :return:
        """
        return self.db.hkeys(self.name())

    def all(self):
        """
        获取所有的键值对
        :return:
        """
        return self.db.hgetall(self.name())