#*encoding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options as COptions
from urllib.parse import quote
from pyquery import PyQuery as pq
import pymongo
import time

options = COptions()
options.add_argument('-headless')
browser = webdriver.Chrome(executable_path="D:\PDF\py包\chromedriver_win32\chromedriver.exe")
# iphone x 搜索 界面改变 倒霉
# browser = webdriver.Chrome(executable_path="D:\PDF\py包\chromedriver_win32\chromedriver.exe")
wait = WebDriverWait(browser, 30)
keyword = input("请输入关键词：")
client = pymongo.MongoClient('mongodb://localhost:27017/')
# 指定数据库
# db = client.movie
db = client['taobao']
# 指定集合
# collection = db.movies
collection = db[keyword]
MAX_PAGE = 1


# 获取页面
def index_page(page):
    if keyword:
        print("正在爬取", page, '页')
        try:
            # 将中文转换成url编码
            url = 'https://s.taobao.com/search?q=' + quote(keyword)
            browser.get(url)
            if page > 1:
                input = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input'))
                )
                submit = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit'))
                )
                input.clear()
                input.send_keys(page)
                submit.click()
            wait.until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page))
            )
            return browser.page_source
        except TimeoutException:
            # 超时就重来
            index_page(page)


# 解析 获取
def get_products(page):

    # html = browser.page_source
    html = index_page(page)
    doc = pq(html)
    ps = doc('#mainsrp-itemlist .items .item').items()
    # items = doc('.m-itemlist .items .item').items()
    # print(type(ps))
    # l = len(list(ps))
    # l = len('1212')
    # l1 = list((1,2,3))OK
    # print(list(ps))
    # print(type(ps))
    for item in ps:
        image = 'http:' + item.find('.pic .img').attr('data-src')
        price = item.find('.price').text()
        deal = item.find('.deal-cnt').text()
        title = item.find('.title').text()
        shop = item.find('.shop').text()
        location = item.find('.location').text()
        product = {
            'image': image,
            'price': price,
            'deal': deal,
            'title': title,
            'shop': shop,
            'location': location
        }
        # print(product)
        save_to_mongo(product)


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
        get_products(i)


main()