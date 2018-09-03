from redis import StrictRedis, ConnectionPool

host = 'localhost'
port = 6379
db = 1
password = '123456'
# 直接连接
redis = StrictRedis(host=host, port=port, db=db, password=password)
# 连接池连接
# cp = ConnectionPool(host=host, port=port, db=db, password=password)
# 连接池从url获取连接信息 password不存在可以省略 三种连接方式
# redis://[:password]@host:port/db   TCP
# rediss://[:password]@host:port/db  TCP+SSL
# unix: // [:password]@/path/to/socket.sock?db =db  UNIX SOCKET
# url = 'redis//@localhost:6379/0'
# url1 = 'redis//@localhost:6379/9'  这个没有用 一直都会链接到第一个数据库
# cp = ConnectionPool.from_url(url)
#
#
# redis = StrictRedis(connection_pool=cp)

# print(redis.set('op', 'add'))
# ##########################################集合操作s######################################################
# 向集合添加元素 已经存在的元素不在添加  返回的是添加成功的数量
print(redis.sadd('set', 1, 2, 3, 4, 5))
# 删除 可以传多个值 返回的是个数
print(redis.srem('set', 1, 2))
# 删除首部一个元素 返回他的值
print(redis.spop('set').decode('utf-8'))
# 从一个集合转移给另一个集合  转移给自己也行 返回是否成功
print(redis.smove('set', 'set1', 1))
# 元素个数
print(redis.scard('set'))
# 返回 判断是否是集合元素  整型和字符串可以互通
print(redis.sismember('set', '5'))


# 返回两个集合 的 交集 元素 用{}输出set
print(redis.sinter('set', 'set1'))
# 得出交集 并保存到指定集合中 第一个参数：指定集合 后面是两个集合的数组 返回数量
print(redis.sinterstore('set2', ['set', 'set1']))


# 得到并集 返回set
print(redis.sunion('set', 'set1', 'set3'))
# 得出并集 并保存到指定集合中 第一个参数：指定集合 后面是两个集合的数组 返回数量
print(redis.sunionstore('set3', ['set', 'set1']))


# 得到差集 返回set
print(redis.sdiff('set', 'set1', 'set4'))
# 得出差集集 并保存到指定集合中 第一个参数：指定集合 后面是两个集合的数组 返回数量
print(redis.sdiffstore('set4', ['set', 'set1']))

# 返回集合的所有元素
print(redis.smembers('set'))

# 返回随机元素
print(redis.srandmember('set'))