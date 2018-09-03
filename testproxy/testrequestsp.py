import socket
# import socks
import requests


proxy_ip = '61.144.105.204:9797'
proxy_ips = '122.72.18.35:80'
# 需要认证的代理
proxy_iprz = 'username:password@61.144.105.204:9797'
proxies = ({
    'http': 'http://' + proxy_ip,
    'https': 'https://' + proxy_ips,
})

try:
    response = requests.get('https://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)