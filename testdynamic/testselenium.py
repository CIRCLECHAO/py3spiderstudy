from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options as COptions

options = COptions()
options.add_argument('-headless')
browser = webdriver.Chrome(executable_path="D:\PDF\py包\chromedriver_win32\chromedriver.exe",
                          chrome_options=options)

# browser = webdriver.Chrome(executable_path="D:\PDF\py包\chromedriver_win32\chromedriver.exe")
try:
    browser.get("https://www.baidu.com")
    input = browser.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    # 这个BY.ID指的是通过id查找元素 也可以写在方法名_by_id都可以的
    wait.until(ec.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
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
