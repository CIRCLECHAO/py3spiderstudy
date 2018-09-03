import socket
# import socks
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options as COptions


proxy_ip = '61.144.105.204:9797'
proxy_ips = '122.72.18.35:80'
# 需要认证的代理
proxy_iprz = 'username:password@61.144.105.204:9797'
proxies = ({
    'http': 'http://' + proxy_ip,
    'https': 'https://' + proxy_ips,
})

options = webdriver.ChromeOptions()
print(proxies['https'])
options.add_argument('--proxy-server=' + proxies['https'])
# options.add_argument('--headless')
browser = webdriver.Chrome(executable_path="D:\PDF\py包\chromedriver_win32\chromedriver.exe",
                          chrome_options=options)
browser.get('https://www.httpbin.org/get')
# print(browser.page_source)