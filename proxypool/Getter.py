from proxypool.testproxypool import RedisClient
from proxypool.testproxymeta import Crawler


POOL_UPPER_THRESHOLD = 10000


# 获取代理类
class Getter():
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()

    def is_over_threadshold(self):
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print('获取器开始执行：')
        if not self.is_over_threadshold():
            # 遍历crawel的方法 执行
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_label]
                proxies = self.crawler.get_proxies(callback)
                for proxy in proxies:
                    self.redis.add(proxy)
        print("获取完成！")


# if __name__ == '__main__':
#     s = Getter()
#     s.run()