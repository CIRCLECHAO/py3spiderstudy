import socket
# import socks
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_ip = '61.144.105.204:9797'
proxy_ips = '122.72.18.35:80'
# 需要认证的代理
proxy_iprz = 'username:password@61.144.105.204:9797'
proxy_handler = ProxyHandler({
    'http': 'http://' + proxy_ip,
    'https': 'https://' + proxy_ips,
})
opener = build_opener(proxy_handler)
try:
    # response = opener.open("https://www.httpbin.org/get")
    response = opener.open("https://www.httpbin.org/get")
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)