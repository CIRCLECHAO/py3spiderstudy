from redis import StrictRedis, ConnectionPool

host = 'localhost'
port = 6379
db = 3
password = '123456'
# 直接连接
redis = StrictRedis(host=host, port=port, db=db, password=password)

# ##########################################哈希表 散列表h######################################################
# 向散列中添加映射 键值对类型随意  返回处理的数量
print(redis.hset('h', 1, 1))
print(redis.hset('h', 'h1', 'hh1'))
print(redis.hset('h', '1', '1'))  # 字符串等同于数字 无法重复插入
print(redis.hset('h', '1', '2'))  #

# 只向不存在的键添加 存在则不处理 返回处理的数量
print(redis.hsetnx('h', 'nx_data', 12))
print(redis.hsetnx('h', 'nx_data', 13))
print(redis.hsetnx('h', 'nx_data1', 'ee'))
print(redis.hsetnx('h', 'nx_data1', '2.5'))

# 根据键获取值
print(redis.hget('h', '1').decode('utf-8'))

# 根据多个键获取多个值
print(redis.hmget('h', ['1', 'nx_data']))

# 将对应键的值增加 非整型报错 增量非整型也报错 默认为1
print(redis.hincrby('h', 'nx_data', amount=1))

# 将对应键的值增加 允许浮点型
print(redis.hincrbyfloat('h', 'nx_data1', amount=1.5))

# 是否存在值
print(redis.hexists('h', 'jj'))
print(redis.hexists('h', '1'))

# 删除 不存在就返回0  返回删除的数量
print(redis.hdel('h', ['1']))

# 哈希表的长度
print(redis.hlen('h'))

# 获取所有的键名
print(redis.hkeys('h'))

# 获取所有的值
print(redis.hvals('h'))

# 获取所有键值对
print(redis.hgetall('h'))