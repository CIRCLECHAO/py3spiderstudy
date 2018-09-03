from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options as COptions
import time

# options = COptions()
# options.add_argument('-headless')
# browser = webdriver.Chrome(executable_path="D:\PDF\py包\chromedriver_win32\chromedriver.exe",
#                           chrome_options=options)

browser = webdriver.Chrome(executable_path="D:\PDF\py包\chromedriver_win32\chromedriver.exe")
browser.get('http://www.zhihu.com/explore')
# time.sleep(1)
# browser.get('http://www.taobao.com')
# time.sleep(1)
# browser.get('http://www.sansung.com')
# # 回退
# time.sleep(2)
# browser.back()
# time.sleep(2)
# # 前进
# browser.forward()
# time.sleep(1)
# browser.close()
# 获取cookie
print(browser.get_cookies())
# 添加cookie  value不能为数字
print(browser.add_cookie({'name':'1', 'domain':'www.zhihu.com', 'value': 'chinese'}))
print(browser.get_cookies())
# 删除cookies
browser.delete_all_cookies()
print(browser.get_cookies())
