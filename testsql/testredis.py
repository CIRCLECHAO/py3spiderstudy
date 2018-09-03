from redis import StrictRedis, ConnectionPool

host = 'localhost'
port = 6379
db = 0
password = '123456'
# 直接连接
# redis = StrictRedis(host=host, port=port, db=db, password=password)
# 连接池连接
cp = ConnectionPool(host=host, port=port, db=db, password=password)
# 连接池从url获取连接信息 password不存在可以省略 三种连接方式
# redis://[:password]@host:port/db   TCP
# rediss://[:password]@host:port/db  TCP+SSL
# unix: // [:password]@/path/to/socket.sock?db =db  UNIX SOCKET
# url = 'redis://:123456@localhost:6379/0'
url1 = 'redis://:123456@localhost:6379/1'
# cp = ConnectionPool.from_url(url)
cp1 = ConnectionPool.from_url(url1)


redis = StrictRedis(connection_pool=cp)
redis1 = StrictRedis(connection_pool=cp1)

print(redis.get('name'))
# ##########################################方法########################################################
# 键是否存在
print(redis.exists('name'))
# 删除
print(redis.delete('name'))
print(redis.set('name', 'bob'))
# 类型
print(redis.type('name'))
# 匹配
print(redis.keys('n*'))
# 随机
print(redis.randomkey())
# 重命名键名
print(redis.rename('name', 'nickname'))
# 获取键的数目
print(redis.dbsize())
# 设定键的过期时间 单位 秒
# print(redis.expire('nickname', 2))
# 获取键的过期时间
print(redis.ttl('nickname'))
# 键移动数据库  不要设置过期时间 否则 =来不及=move
# print(redis.move('nickname', 1))
# 删除当前数据库所有键值
# print(redis.flushdb())
# 删除所有数据库所有键
# print(redis.flushall())
# 给赋值 并且返回原来的值
print(redis.getset('nickname', 'newname'))
# 返回多个键值对应的value
print(redis.mget(['nickname', 'name2']))
# 批量赋值
print(redis.mset({'n': 1, 'x': 2}))
# 如果键不存在就设置值 否则不设置值  （只新增 不更新）第二条不起作用
print(redis.setnx('ni', 'wo'))
print(redis.setnx('ni', '2'))
# 如果键不存在就设置值 否则不设置值  （只新增 不更新）第二条不起作用 批量
print(redis.msetnx({'nix': 1, 'wox': 2}))
print(redis.msetnx({'nix': 3, 'wox': 4}))
# 设置键的值以及过期时间  可以新增以及更新
print(redis.setex('wo', 120, 'Lucy'))
# 往value插入字符串 如果字符不存在会新建 如果位置不存在 会为空类型变成binary 如果是0就可以
print(redis.setrange('ni', 2, 'hao'))
print(redis.setrange('nini', 2, 'hao'))
# 增长 默认1
print(redis.incr('nix', 10))
# 减少 默认1
print(redis.decr('nix', 10))
# 值的最后位置追加
print(redis.append('nickname', 'nickname'))
# 获取子串 开始 以及结束 不传就是 -1
print(redis.substr('nickname', 3))
# 获取子串 开始 以及结束 不传就是 报错 也可以是-1
print(redis.getrange('nickname', 4, 5))
