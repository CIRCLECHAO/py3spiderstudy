from selenium import webdriver
from selenium.webdriver.common.by import By
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
    browser.get("https://www.taobao.com")
    input = browser.find_element(By.ID, 'q')
    input.send_keys('iPhone')
    time.sleep(1)
    input.send_keys('iPad')
    button = browser.find_element(By.CLASS_NAME, 'btn-search')
    button.click()
finally:
    browser.close()


# WebDriver提供了8中定位一组元素的方法
# find_elements_by_id()
# find_elements_by_name()
# find_elements_by_class_name()
# find_elements_by_tag_name()
# find_elements_by_link_text()
# find_elements_by_partial_link_text()
# find_element_by_xpath() 根据xpath获取
# find_element_by_css_selector() 根据css获取
