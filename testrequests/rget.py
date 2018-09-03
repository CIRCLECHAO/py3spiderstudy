import requests
re = requests.get("http://www.baidu.com")
print(re)
print(re.status_code)
print(re.cookies)
# print(re.text)
# print(re.content) #b数据

# 传参
data = {
    'name': 'germey',
    'age': 22
}
r = requests.get("http://httpbin.org/get", params=data)

print(type(r.text))
print(r.text)
print(type(r.json()))
print(r.json())

# 添加headers
headers = {
    'User-Agent': 'MOzilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebkit/537.36 (KHTML like Gecko)'
                  'Chrome/52.0.2743 Safari/537.36'
}
r = requests.get('https://www.zhihu.com/explore', headers=headers)
print(r.text)