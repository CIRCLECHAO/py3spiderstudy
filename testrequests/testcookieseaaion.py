import requests
import urllib3
# 复制登录后的cookie 模拟登录 如果网页已经退出就不起作用
# headers = {
#     'Cookie': '',
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
#                   '(KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
# }
# r = requests.get("https://www.zhihu.com", headers=headers);
# print(r.text)

# cookies无法会话维持
# requests.get("http://httpbin.org/cookies/set/number/123456789")
# r = requests.get('http://httpbin.org/cookies')
# print(r.text)
# # session可以维持会话
# s = requests.Session()
# s.get("http://httpbin.org/cookies/set/number/123456789")
# r = s.get("http://httpbin.org/cookies")
# print(r.text)

# SSL验证 加vertify参数
# urllib3 pythons自带的直接导入
urllib3.disable_warnings()
response = requests.get("https://www.12306.cn", verify=False)
print(response.status_code)