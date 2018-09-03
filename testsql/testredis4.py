from redis import StrictRedis, ConnectionPool

host = 'localhost'
port = 6379
db = 2
password = '123456'
# 直接连接
redis = StrictRedis(host=host, port=port, db=db, password=password)

# ##########################################有序集合操作z######################################################
# 添加元素 如果元素已经存在 则更新排序值  第一个是score（排序）  第二个是值
print(redis.zadd('zset', 1, 'd', 0.5, '123'))
# 删除  可以传多个
redis.zadd('zset', 1, 'ds')
print(redis.zrem('zset', 'ds', 'd'))
# 无 增添 有则将其score增加数字amount 默认1 返回 float 的amount
print(redis.zincrby('zset', 'dd', amount=1))

# 返回在zset中的下标 从0开始的 从小到大排列
print(redis.zrank('zset', 'dd'))
# 返回在zset中的下标 从0开始的 从大到小排列
print(redis.zrevrank('zset', 'dd'))

# 返回在score区间的元素 包含上下线
print(redis.zrangebyscore('zset', 0.5, 100))

# 返回在score区间的元素 数量
print(redis.zcount('zset', 0.5, 100))

# 返回元素 数量
print(redis.zcard('zset'))

# 删除元素下标在范围内的元素  包含上下线 返回删除数量
# print(redis.zremrangebyrank('zset', 0, 1))

# 删除score在范围内的元素  包含上下线 返回删除数量
print(redis.zremrangebyrank('zset', 0, 0))