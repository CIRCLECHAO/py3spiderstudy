from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit, \
    urljoin, urlencode, parse_qs, parse_qsl, quote, unquote
result = urlparse("http://www.baidu.com/index.html;user?id=4#comment")
# 可以指定 scheme  如果url中不含有才会生效 allow_frarments不允许则将fragment放进query或者前面
print(type(result), result, sep="\n")
print(result[0])
print(result.scheme)

# 将一个6元素的可迭代对象转换成链接  长度必须是6
data = ['http', 'www.baidu.com', '/index.html', 'user', 'id=4', 'comment']
data1 = ['http', 'www.baidu.com', '/index.html', 'user', 'id=4', '']
data2 = ['http', 'www.baidu.com', '/index.html', 'user', 'id=4']
data3 = ['', 'www.baidu.com', '/index.html', 'user', 'id=4', '']
print(urlunparse(data))
print(urlunparse(data1))
# print(urlunparse(data2))
print(urlunparse(data3))

# urlsplit 不解析param 返回5个
result = urlsplit("http://www.baidu.com/index.html;user?id=4#comment")
print("\n")
print(result)
# 将一个5元素的可迭代对象转换成链接  长度必须是5
data2 = ['http', 'www.baidu.com', '/index.html', 'user', 'id=4']
print("\n")
print(urlunsplit(data2))

# urljoin 补充主链接的scheme netloc  param
print("\n")
print(urljoin("www.baidu.com#comment", 'https://?category=2'))
print(urljoin("www.baidu.com#comment", '?category=2'))
print(urljoin("www.baidu.com#comment", 'https://www.souhu.com?category=2'))

# urlencode 将字典放入链接的param
params = {
    'is': 1,
    'aer': 2,
}
base_url = 'www.baidu,com?'  #问号自己加
print("\n")
url = base_url+urlencode(params)
print(url)
print(parse_qs(url))#字典
print(parse_qsl(url))#元组

# 将中文转换成url编码
keyword = "家家爱"
url = 'http://www.baidu.com?keyword='+quote(keyword)
print(url)
print(unquote(url))