import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
import pymongo
from redis import StrictRedis
import time
import pymysql


base_url = 'https://m.weibo.cn/api/container/getIndex?containerid=2304131720173771_-_' \
           'WEIBO_SECOND_PROFILE_WEIBO'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
          }


# 获取页面
def get_page(page):
    params = {
        'containerid': '2304131720173771_-_WEIBO_SECOND_PROFILE_WEIBO',
        'page_type': '03',
        'page': page,
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print("ERROR", e.args)


# 解析页面
def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            ib = item.get('mblog')
            weibo = {}
            weibo['id'] = ib.get('id')
            weibo['text'] = pq(ib.get('text')).text()
            weibo['attitudes_count'] = ib.get('attitudes_count')
            weibo['comments_count'] = ib.get('comments_count')
            weibo['reposts_count'] = ib.get('reposts_count')
            yield weibo


# mongo保存
def mongo_save_data(collection, data):
    # 新建连接

    collection.insert_one(data)
    num = collection.count()
    print('插入成功，共有 %s 条数据' % num)


# redis保存
def redis_save_data(redis, data):
    # 新建连接
    redis.hsetnx(data['id'], 'id', data['id'])
    redis.hsetnx(data['id'], 'text', data['text'])
    redis.hsetnx(data['id'], 'attitudes_count', data['attitudes_count'])
    redis.hsetnx(data['id'], 'comments_count', data['comments_count'])
    redis.hsetnx(data['id'], 'reposts_count', data['reposts_count'])
    num = redis.dbsize()
    print('插入成功，共有 %s 条数据' % num)


# mysql保存
def mysql_save_data(cursor, data):
    data = {
        'id': data['id'],
        'text': data['text'],
        'attitudes_count': data['attitudes_count'],
        'comments_count': data['comments_count'],
        'reposts_count': data['reposts_count'],
    }
    table = 'weibo'
    keys = ','.join(data.keys())
    values = ','.join(['%s'] * len(data))
    sql = "INSERT INTO {table}({keys}) VALUES ({values})".format(table=table, keys=keys, values=values)
    sql1 = "SELECT * FROM {table} ".format(table=table)
    print(sql1)
    try:
        if cursor.execute(sql, tuple(data.values())):
            # print('insert success')
            db.commit()
            cursor.execute(sql1)
            num = cursor.rowcount
            print('插入成功，共有 %s 条数据' % num)
    except:
        db.rollback()


if __name__ == '__main__':
    database = input('选择储存方式 1 mongo, 2 redis, 3 mysql: ')
    t = time.time()
    for page in range(1, 11):
        json = get_page(page)
        results = parse_page(json)
        if database == "1":
            # 连接mongo
            print('mongo')
            client = pymongo.MongoClient('mongodb://localhost:27017/')
            db = client['movie']
            collection = db['weibo']
            for result in results:
                mongo_save_data(collection, result)
        elif database == "2":
            host = 'localhost'
            port = 6379
            db = 4
            password = '123456'
            # 直接连接
            redis = StrictRedis(host=host, port=port, db=db, password=password)
            for result in results:
                redis_save_data(redis, result)
        elif database == "3":
            host = '127.0.0.1'
            user = 'root'
            password = 'root'
            port = 3306
            db = pymysql.connect(host=host, user=user, password=password, port=port)
            cursor = db.cursor()
            cursor.execute("USE spiders")
            # cursor.execute("CREATE TABLE IF NOT EXISTS weibo (id VARCHAR(255) NOT NULL ,text TEXT(1000), "
            #                "attitudes_count INT(10) , comments_count INT(10), reposts_count INT(10)"
            #                 ",age INT NOT NULL ,PRIMARY KEY(id))")
            for result in results:
                mysql_save_data(cursor, result)

    print("用时 %f s" % (time.time()-t))