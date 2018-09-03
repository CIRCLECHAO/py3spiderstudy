from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'admin'
password = '123456'
url = 'https://www.eolinker.com/#/home/project/inside/api/list?' \
      'projectName=%E9%87%91%E9%94%80%E5%86%A0&projectHashKey=nSaBwS5e7b422a45afe68b37c28946b09d9e47d8aefc273'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)