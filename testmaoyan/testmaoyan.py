import requests
import re
import json


def get_one_page(url):
    proxies = {
        'http': '111.155.116.234:8123',
        'https': '118.31.220.3:8080'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def main(offset):
    url = "https://maoyan.com/board/4?offset="+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)


def parse_one_page(html):
        # 正则表达式进行解析
        pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name">'
                             '<a.*?>(.*?)</a>.*?"star">(.*?)</p>.*?releasetime">(.*?)</p>'
                             '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
        items = re.findall(pattern, html)
        # print(items)
        for item in items:
            # 相当于返回了一个可迭代对象（生成器？   
            yield{
                'index': item[0],
                'image': item[1],
                'title': item[2].strip(),
                'actor': item[3].strip()[3:] if len(item[3]) > 3 else "",
                'time': item[4].strip()[5:] if len(item[4]) > 5 else "",
                'score': item[5].strip() + item[6].strip(),
            }


def write_to_file(content):
    with open('maoyan_10.txt', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


# html = main()
# # print(html)

if __name__ == "__main__":
    for i in range(10):
        main(offset=i*10)