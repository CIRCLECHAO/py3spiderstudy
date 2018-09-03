import urllib.request as ur
import urllib.error as ue
try:
    response = ur.urlopen("https://cuiqingcai.com/index.html")
except ue.HTTPError as e:
    print(e.reason, e.headers, e.code, sep="\n")