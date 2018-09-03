import urllib.request as ur
import urllib.parse as up
import urllib.error as ue
import socket
# response = ur.urlopen("http://www.python.org")
# # print(response.read().decode("utf-8"))
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

# data = bytes(up.urlencode({'world':'hello'}), encoding='utf-8')
# response = ur.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

# try:
#     response = ur.urlopen('http://httpbin.org/post', timeout=0.1)
# except ue.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print("TIME OUT")

# 传入request对象来发出请求
# request = ur.Request('https://python.org')
# response = ur.urlopen(request)
# print(response.read().decode('utf-8'))
# 完整的request参数
url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0(compatible;MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(up.urlencode(dict), encoding='utf-8')
print(data)
# headers也可以用add_header添加   req.add_header(headers)
req = ur.Request(url=url, data=data, headers=headers, method='POST')
response = ur.urlopen(req)
print(response.read().decode('utf-8'))