from redis import StrictRedis, ConnectionPool

host = 'localhost'
port = 6379
db = 0
password = ''
# 直接连接
# redis = StrictRedis(host=host, port=port, db=db, password=password)
# 连接池连接
# cp = ConnectionPool(host=host, port=port, db=db, password=password)
# 连接池从url获取连接信息 password不存在可以省略 三种连接方式
# redis://[:password]@host:port/db   TCP
# rediss://[:password]@host:port/db  TCP+SSL
# unix: // [:password]@/path/to/socket.sock?db =db  UNIX SOCKET
url = 'redis://:123456@localhost:6379/0'
url1 = 'redis://:123456@localhost:6379/1'
cp = ConnectionPool.from_url(url)
cp1 = ConnectionPool.from_url(url1)


redis = StrictRedis(connection_pool=cp)
redis1 = StrictRedis(connection_pool=cp1)

# print(redis.set('op', 'add'))
# ##########################################列表操作l######################################################
# 添加多个值在末尾  必须是一个list否则会报错  右侧push
# print(redis.rpush('op', 1, 2))
# print(redis.rpush('op', 'del', 'add'))
# 添加多个值在开始  必须是一个list否则会报错  左侧push
# print(redis.lpush('op', '3', '4'))
# 返回列表长度
print(redis.llen('op'))
# 截取列表的数据  结尾不能省略  返回一个数组
# print(redis.lrange('op', 1, 4))
# 从头部开始截取  会导致 数据只留下截取的部分 下标从0开始 最后一个参数也是下标
print(redis.ltrim('op', 0, 4))
# 根据索引返回列表值 下标从0开始 超出范围就是None
print(redis.lindex('op', 1).decode('utf-8'))
# 按照列表下标赋值 越界报错
print(redis.lset('op', 1, '新的赋值'))
# 删除多个值为 某个的 列表数据   参数： 列表名  删除个数(至少删除一个 传小于1的数字就是等于1)   value
redis.lpush('op', '测试删除')
print(redis.lrem('op', -1, '测试删除'))
# 删除并且返回列表头部元素
redis.lpush('op', '测试lpop')
print(redis.lpop('op').decode('utf-8'))
# 删除并且返回列表尾部元素
redis.rpush('op', '测试rpop')
print(redis.rpop('op').decode('utf-8'))
# Redis Brpop 命令移出并获取列表的最后一个元素， blpop也是存在的
# 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止 返回列表名 以及pop元素名
print(redis.brpop('op1', timeout=10))
print(redis.lpush('op1', 'RR'))
# rpoplpush 顾名思义  一个列表的末元素删除
#   最末的元素添加到一个列表最头部 可以选同一个
print(redis.rpoplpush('op', 'op').decode('utf-8'))