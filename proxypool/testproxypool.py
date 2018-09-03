from redis import StrictRedis, ConnectionPool
from random import choice
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_KEY = 'proxies'
REDIS_PASSWORD = '123456'


# 数据库操作类
class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        cp = ConnectionPool(host=host, port=port, password=password)
        self.db = StrictRedis(connection_pool=cp)

    def add(self, proxy, score=INITIAL_SCORE):
        # 不存在重复成员则执行添加
        if not self.db.zscore(REDIS_KEY, proxy):
            return self.db.zadd(REDIS_KEY, score, proxy)

    def random(self):
        # 获取有效代理 先获取最高分代理 不存在按照分数排名获取
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrangebyscore(REDIS_KEY, 0, 100)
            if len(result):
                return choice(result)
            else:
                raise Exception

    def decrease(self, proxy):
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print('代理', proxy, score, '分数-2')
            return self.db.zincrby(REDIS_KEY, proxy, -2)
        else:
            print('代理', proxy, score, '移除')
            return self.db.zrem(REDIS_KEY, proxy)

    def exists(self, proxy):
            # 判断是否存在
            return not self.db.zscore(REDIS_KEY, proxy) is None

    def max(self, proxy):
            # 代理分数最大化
            print('代理', proxy, '可用', '设置为', MAX_SCORE)
            # 添加元素 如果元素已经存在 则更新排序值  第一个是score（排序）  第二个是值
            return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)

    def count(self):
            # 计数
            return self.db.zcard(REDIS_KEY)

    def all(self):
            # 全部数据
            return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)
