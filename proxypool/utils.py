# *encoding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options as COptions
import time


options = COptions()
options.add_argument('-headless')
browser = webdriver.Chrome(executable_path="D:\PDF\py包\chromedriver_win32\chromedriver.exe",
                          chrome_options=options)
wait = WebDriverWait(browser, 30)

MAX_PAGE = 100


# 获取页面
def get_page(url, op=''):
        try:
            # 将中文转换成url编码
            print(url)
            time.sleep(2)
            browser.get(url)
            print('抓取', url, '成功')
            return browser.page_source
        except TimeoutException:
            # 超时就重来
            get_page(url)
