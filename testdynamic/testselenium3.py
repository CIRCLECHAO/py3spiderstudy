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
    url = "https://www.zhangxinxu.com/study/201102/html5-drag-and-drop.html"
    browser.get(url)
    # browser.switch_to.frame("iframeResult") 没什么反应
    source = browser.find_element(By.CSS_SELECTOR, ".draglist:last-child")
    target = browser.find_element(By.CSS_SELECTOR, ".dustbin:first-child")
    actions = ActionChains(browser)
    actions.drag_and_drop(source, target)
    actions.perform()
finally:
    browser.close()

# 调用JS
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("滚到底部了")')

