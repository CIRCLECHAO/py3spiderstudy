import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool


def get_page(offset):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'auto',
        'count': 20,
        'cur_tab': 1,
        'from': 'search_tab'
    }

    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_list')
            if images:
                for image in images:
                    yield {
                        'title': title,
                        'image': 'http:' + image.get('url')
                    }


def save_img(item):
    dir = 'PIC/'+keyword+"/"+item.get('title')
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(dir,
                                                 md5(response.content).hexdigest(), 'jpg')
            # print(file_path)
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('已下载', file_path)
    except requests.ConnectionError:
        print('下载失败')


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_img(item)


GROUP_START = 1
GROUP_END = 5

keyword = input("请输入关键词搜索：")
if __name__ == "__main__":
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END+1)])
    pool.map(main, groups)
    pool.close()
    pool.join()