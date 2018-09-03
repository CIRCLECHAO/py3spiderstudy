import requests
from pyquery import PyQuery as pq
# 测试保存到txt
url = "http://www.zhihu.com/explore"
# 访问网址
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get("https://www.zhihu.com/explore", headers=headers)
html = r.text
# 解析对象
doc = pq(html)
# 获取需要的信息
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    # file操作
    file = open('files/explore.txt', 'a', encoding='utf-8')
    # Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。a 换行 b 换行 c 换行
    file.write('\n'.join([question, author, answer]))
    file.write("\n"+'='*100+"\n")
    file.close()

