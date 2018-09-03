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
# 更新数据update 官方推荐 update_one update_many 配合$set使用
# condition = {'最终得分': -1}
# movie = collection.find_one(condition)
# print(movie['总的办公盒子'])
# movie['总的办公盒子'] = "1"
# re = collection.update(condition, movie)
# print(re)
# print(movie['总的办公盒子'])
# movie['总的办公盒子'] = "推荐"
# re = collection.update_one(condition, {'$set': movie})
# print(re)
# print(movie['总的办公盒子'])
# 批量更新
condition = {'最终得分': {'$lt': 0}}
re = collection.update_many(condition, {'$inc': {'最终得分': 1}})
print(re.matched_count, re.modified_count)
# 删除 remove  官方推荐 delete_one delete_many
r1 = collection.remove({'电影标题': '八只鸡'})
print(r1)
r2 = collection.delete_one({'电影标题': '村戏'})
print(r2.deleted_count)
r3 = collection.delete_many({'电影标题': '神奇马戏团'})
print(r3.deleted_count)
