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
try:
    # browser.get("https://www.taobao.com")
    url = "https://www.zhihu.com/explore"
    browser.get(url)
    # 延时等待 隐式等待 固定的时间
    # browser.implicitly_wait(1)
    # 显示等待  指定要查找的节点 规定时间未查出报超时异常
    wait = WebDriverWait(browser, 3)
    # 等待节点出现
    input = wait.until(ec.presence_of_element_located((By.ID, 'asdfg')))
    # title是某
    input = wait.until(ec.title_is('标题'))
    # title包含
    input = wait.until(ec.title_contains('标题'))
    #节点可见
    input = wait.until(ec.visibility_of_element_located((By.ID, 'asdfg')))

    # logo = browser.find_element(By.ID, 'zh-top-link-logo')
    # input = browser.find_element(By.CLASS_NAME, 'zu-top-add-question')
    print(input)
    # print(logo)
    # 根据属性名获取值
    # print(logo.get_attribute('class'))
    # # 获取文本 id 位置 标签名  大小
    # print(input.text)
    # print(input.id)
    # print(input.location)
    # print(input.tag_name)
    # print(input.size)

finally:
    # browser.close()
    print('手动关闭谢谢')



