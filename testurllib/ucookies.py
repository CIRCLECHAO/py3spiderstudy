import http.cookiejar as hcj
import urllib.request as ur

# 保存cookie到文件MozillaCookieJar格式
filename = 'cookies.txt'
cookie1 = hcj.MozillaCookieJar(filename)
handler1 = ur.HTTPCookieProcessor(cookie1)
opener1 = ur.build_opener(handler1)
response = opener1.open("http://www.baidu.com")
cookie1.save(ignore_discard=True, ignore_expires=True)

# 保存cookie到文件LWPCookieJar格式
filename = 'cookiesLW.txt'
cookie2 = hcj.LWPCookieJar(filename)
handler2 = ur.HTTPCookieProcessor(cookie2)
opener2 = ur.build_opener(handler2)
response = opener2.open("http://www.baidu.com")
cookie2.save(ignore_discard=True, ignore_expires=True)

# 读取文件中的cookie
cookie3 = hcj.LWPCookieJar()
cookie3.load('cookiesLW.txt', ignore_expires=True, ignore_discard=True)
handler = ur.HTTPCookieProcessor(cookie3)
opener = ur.build_opener(handler)
response = opener.open("http://www.baidu.com")
print(response.read().decode('utf-8'))

# 输出获取的cookie
# cookie = hcj.CookieJar()
# handler = ur.HTTPCookieProcessor(cookie)
# opener = ur.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# for item in cookie:
#     print(item.name+"="+item.value)