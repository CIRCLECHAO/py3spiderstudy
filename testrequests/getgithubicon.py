import requests
import re
r = requests.get("http://static.fclmw.cn/images/site_img/logo.png")
# print(r.text)
# print(r.content)
with open("fclmw.png", 'wb') as f:
    f.write(r.content)

# 上传文件
files = {'file': open('fclmw.png', 'rb')}
r = requests.post("https://httpbin.org/post", files=files)
print(r.text)