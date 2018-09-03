import requests
from requests import Request, Session
proxies = {
    'http': '111.155.116.234:8123',
    'https': '118.31.220.3:8080'
}
# 使用高匿名的代理才起作用 使用透明的没反应
# r = requests.get("http://www.taobao.com", proxies=proxies)
# r = requests.get("https://www.taobao.com")
# print(r.text)

# prepared request
url = "http://httpbin.org/post"
data = {
    'name': 'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
