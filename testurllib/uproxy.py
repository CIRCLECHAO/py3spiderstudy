from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener
proxy_handler = ProxyHandler({
    'http': 'http://114.113.126.86:80',
    'https': 'https://122.72.18.35:80',
})
opener = build_opener(proxy_handler)
try:
    response = opener.open("http://www.httpbin.org")
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)