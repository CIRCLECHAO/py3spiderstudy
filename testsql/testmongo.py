import pymongo
# 新建连接
# client = pymongo.MongoClient(host='localhost', port=27017)
client = pymongo.MongoClient('mongodb://localhost:27017/')
# 指定数据库
# db = client.movie
db = client['movie']
# 指定集合
# collection = db.movies
collection = db['movies']
# 插入数据
movie = {
    '电影ID': '1',
    '电影标题': '哈哈哈',
    '最终得分': '12',
}
movie1 = {
    '电影ID': '2',
    '电影标题': '哈哈哈',
    '最终得分': '12',
}
movie2 = {
    '电影ID': '3',
    '电影标题': '哈哈哈',
    '最终得分': '12',
}
# 也可传入列表 插入多条
# result = collection.insert(movie)
# resultm = collection.insert([movie, movie1, movie2])
# print(resultm)
# 官方推荐 insert_one 传入一个字典 insert_many 传入一个字典列表

# 查询数据 单条
# result = collection.find_one({'电影标题': '哈哈哈'})
# print(result)
# print('\n')

# 查询数据 多条
# result_many = collection.find({'最终得分': '12'})
# for results in result_many:
#     print(results)

# 查询条件 以及 正则查询
# result1 = collection.find({'最终得分': {'$lt': 9}})  # 小于9的
# print(result1)
# result2 = collection.find({'最终得分': {'$gt': 9}})  # 小于9的
# print(result2)
# result3 = collection.find({'最终得分': {'$lte': 9}})  # 小于等于9的
# print(result3)
# result4 = collection.find({'最终得分': {'$lt': 9}})  # 小于9的
# print(result4)
# result5 = collection.find({'最终得分': {'$gte': 9}})  # 大于等于9
# print(result5)
# result6 = collection.find({'最终得分': {'$ne': 9}})  # 不等于9的
# print(result6)
# result7 = collection.find({'最终得分': {'$in': [8, 9]}})  # 范围内8,9
# print(result7)
# result8 = collection.find({'最终得分': {'$nin': [7, 8]}})  # 不在范围内8,9
# print(result8)
# result9 = collection.find({'最终得分': {'$regex': '^\d+'}})  # 正则
# print(result9)
# 计数 find().count()
# resultc = collection.find({'最终得分': {'$lt': 7}}).count()  # 正则
# print(resultc)
# 排序 ASCENDING DESCENDING
# rp = collection.find({'最终得分': {'$lt': 7}}).sort('最终得分', pymongo.ASCENDING)  # 正序
# print([str(r['最终得分'])+r['电影标题'] for r in rp])

# 偏移skip 以及 限制limit 表示从结果的第几条开始 取几条
rsl = collection.find({'最终得分': {'$lt': 7}}).sort('最终得分', pymongo.ASCENDING).skip(3).limit(5)  # 正序
# 一定要记得打印加[]
print([r['最终得分'] for r in rsl])