from cookiespool.RedisClient import RedisClient
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as COptions
from selenium.webdriver import DesiredCapabilities
from cookiespool.config import *
from cookiespool.WeiboCookies import WeiboCookies
from cookiespool.ZhihuCookies import ZhihuCookies
import json


class CookieGenerator(object):

    def __init__(self, website="default"):
        """
               父类, 初始化一些对象
               :param website: 名称
        """
        self.website = website
        self.cookies_db = RedisClient('cookies', self.website)
        self.account_db = RedisClient('accounts', self.website)
        self.init_browser()

    def __del__(self):
        self.close()

    def init_browser(self):
        """
        通过browser参数初始化全局浏览器供模拟登录使用
        :return:
        """
        if BROWSER_TYPE == 'PhantomJS':
            caps = DesiredCapabilities.PHANTOMJS
            caps["phantomjs.page.settings.userAgent"] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3)' \
                                                        ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133' \
                                                        ' Safari/537.36'
            self.browser = webdriver.PhantomJS(desired_capabilities=caps)
            self.browser.set_window_size(1400, 500)
        elif BROWSER_TYPE == 'Chrome':
            options = COptions()
            # options.add_argument('-headless')
            self.browser = webdriver.Chrome(executable_path="D:\PDF\py包\chromedriver_win32\chromedriver.exe",chrome_options=options)
        else:
            self.browser = None

    def new_cookies(self, username, password):
        """
        生成新的cookies 子类重写
        :param username: 用户名
        :param password: 密码
        :return:
        """
        raise NotImplementedError

    def process_cookies(self, cookies):
        """
        处理cookies
        :param cookies:
        :return:
        """
        dict = {}
        for cookie in cookies:
            dict[cookie['name']] = cookie['value']
        return dict

    def run(self):
        """
        得到所有帐户 依次模拟登录
        :return:
        """
        accounts_names = self.account_db.usernames()
        cookies_names = self.cookies_db.usernames()

        for username in accounts_names:
            if username not in cookies_names:
                password = self.account_db.get(username)
                print('正在生成cookies', '账户：', username, '密码：', password)
                result = self.new_cookies(username, password)
                print(result)
                if result.get('status') == 1:
                    cookies = self.process_cookies(result.get('content'))
                    print('成功获取到cookies', cookies)
                    if self.cookies_db.set(username, json.dumps(cookies)):
                        print('保存成功', cookies)
                elif result.get('status') == 2:
                    print(result.get('content'))
                    if self.account_db.delete(username):
                        print('登录名密码无效 已经删除')
                else:
                    print(result.get('content'))
            else:
                print("所有帐户均已获取到cookies")

    def close(self):
        """
        关闭
        :return:
        """
        try:
            print("CLOSE BROWSER")
            self.browser.close()
            del self.browser
        except TypeError:
            print('Browser not opened')


class WeiboCookiesGenerator(CookieGenerator):
    def __init__(self, website='weibo'):
        CookieGenerator.__init__(self, website)
        self.website = website

    def new_cookies(self, username, password):
        """
        生成cookies
        :param username:
        :param password:
        :return:
        """
        return WeiboCookies(username, password, self.browser).main()


#     知乎生成器
class ZhihuCookiesGenerator(CookieGenerator):
    def __init__(self, website='zhihu'):
        CookieGenerator.__init__(self, website)
        self.website = website

    def new_cookies(self, username, password):
        return ZhihuCookies(username, password, self.browser).main()


if __name__ == "__main__":
    generator = WeiboCookiesGenerator()
    generator.run()