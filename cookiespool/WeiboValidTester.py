import json
import requests
from requests.exceptions import ConnectionError
from cookiespool.ValidTester import ValidTester
from cookiespool.config import *


class WeiboValidTester(ValidTester):
    def __init__(self, website='weibo'):
        ValidTester.__init__(self,website)

    def test(self, username, cookies):
        print('正在测试cookies, 用户名：', username)
        try:
            cookies = json.loads(cookies)
        except TypeError:
            print('cookies不合法', username)
            self.cookies_db.delete(username)
            print('删除cookies', username)
            return
        try:
            test_url = TEST_URL_MAP[self.website]
            response = requests.get(test_url, cookies=cookies, timeout=5, allow_redirects=False)
            if response.status_code == 200:
                print('cookies有效', username)
                print('部分测试结果', response.text[0:50])
            else:
                print(response.status_code, response.headers)
                print('cookies失效', username)
                self.cookies_db.delete(username)
                print('删除cookies', username)
        except ConnectionError as e:
            print('异常', e.args)
