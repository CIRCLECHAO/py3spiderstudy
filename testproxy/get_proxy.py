# *encoding=utf-8
# 批量获取代理 并存储到mongoDB
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options as COptions
import pymongo
import time
import datetime
from bs4 import BeautifulSoup


options = COptions()
options.add_argument('-headless')
browser = webdriver.Chrome(executable_path="D:\PDF\py包\chromedriver_win32\chromedriver.exe",
                          chrome_options=options)
# iphone x 搜索 界面改变 倒霉
# browser = webdriver.Chrome(executable_path="D:\PDF\py包\chromedriver_win32\chromedriver.exe")
wait = WebDriverWait(browser, 30)
# keyword = input("请输入关键词：")
client = pymongo.MongoClient('mongodb://localhost:27017/')
# 指定数据库
# db = client.movie
db = client['proxy']
# 指定集合
# collection = db.movies
y = datetime.datetime.now().year
m = datetime.datetime.now().month
d = datetime.datetime.now().day
collection = db['proxy'+str(y)+str(m)+str(d)]
MAX_PAGE = 100


# 获取页面
def index_page(page):
        print("正在爬取", page, '页')
        try:
            # 将中文转换成url编码
            url = 'https://www.kuaidaili.com/free/inha/' + str(page)
            print(url)
            time.sleep(2)
            browser.get(url)
            get_proxys()
        except TimeoutException:
            # 超时就重来
            index_page(page)


# 解析 获取
def get_proxys():
    html = browser.page_source
    # print(html)
    # doc = pq(html)
    # ps = doc('tr').items()
    # print(len(list(ps)))
    # for item in ps:
    #         ip = item.find('tr [data-title="IP"]').text()
    #         # port = item.find('tr [data-title="PORT"]').text()
    #         # nmd = item.find('tr [data-title="匿名度"]').text()
    #         # type = item.find('tr [data-title="类型"]').text()
    #         # position = item.find('tr [data-title="位置"]').text()
    #         # speed = item.find('tr [data-title="响应速度"]').text()
    #         # last_time = item.find('tr [data-title="最后验证时间"]').text()
    #
    #         proxy = {
    #             'ip': ip,
    #             # 'port': port,
    #             # 'nmd': nmd,
    #             # 'type': type,
    #             # 'position': position,
    #             # 'speed': speed,
    #             # 'last_time': last_time,
    #         }
    #         print(proxy)
    #         save_to_mongo(proxy)
    soup = BeautifulSoup(html, 'lxml')
    for i, child in enumerate(soup.tbody.children):
        # print(child)
        soup1 = BeautifulSoup(str(child), 'lxml')
        for child1 in enumerate(soup1.children):
            print(child1)
            soup2 = BeautifulSoup(str(child1), 'lxml')
            ip = soup2.select('td[data-title="IP"]')[0].get_text()
            port = soup2.select('td[data-title="PORT"]')[0].get_text()
            nmd = soup2.select('td[data-title="匿名度"]')[0].get_text()
            type = soup2.select('td[data-title="类型"]')[0].get_text()
            position = soup2.select('td[data-title="位置"]')[0].get_text()
            speed = soup2.select('td[data-title="响应速度"]')[0].get_text()
            last_time = soup2.select('td[data-title="最后验证时间"]')[0].get_text()
            proxy = {
                'ip': ip,
                'port': port,
                'nmd': nmd,
                'type': type,
                'position': position,
                'speed': speed,
                'last_time': last_time,
            }
            print(proxy)
            save_to_mongo(proxy)


# 保存数据
def save_to_mongo(product):
    try:
        if collection.insert_one(product):
            print('保存成功')
    except Exception:
        print('保存失败')


# 实行
def main():
    for i in range(1, MAX_PAGE+1):
        index_page(i)


main()