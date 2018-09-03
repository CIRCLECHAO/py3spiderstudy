import asyncio
import aiohttp
import time
import sys
try:
    from aiohttp import ClientError
except:
    from aiohttp import ClientProxyConnectionError as ProxyConnectionError
from .testproxypool import RedisClient
import aiohttp

# 测试类
VALID_STATUS_CODE = [200]
TEST_URL = 'http://www.baidu.com'
BATCH_TEST_SIZE = 100


class Tester(object):
    def __init__(self):
        self.redis = RedisClient()

    # 方法异步
    async def test_single_proxy(self, proxy):
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                # isinstance() 与 type() 区别：
                # type() 不会认为子类是一种父类类型，不考虑继承关系。
                # isinstance() 会认为子类是一种父类类型，考虑继承关系。
                if isinstance(proxy, bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://' + proxy
                print('正在测试', proxy)
                async with session.get(TEST_URL, proxy=real_proxy, timeout=15) as response:
                    if response.status in VALID_STATUS_CODE:
                        self.redis.max(proxy)
                        print('代理可用', proxy)
                    else:
                        self.redis.decrease(proxy)
                        print('响应码不合法', proxy)
            except Exception as e:
                self.redis.decrease(proxy)
                print('代理请求失败', proxy)

    def run(self):
        print('测试开始运行：')
        try:
            proxies = self.redis.all()
            loop = asyncio.get_event_loop()
            # 批量测试 最后参数：步长
            for i in range(0, len(proxies), BATCH_TEST_SIZE):
                test_proxies = proxies[i:i + BATCH_TEST_SIZE]
                tasks = [self.test_single_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks))
                time.sleep(5)
        except Exception as e:
            print('测试器发生错误', e.args)
        finally:
            print('测试完成！')