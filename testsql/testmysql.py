import pymysql

host = '127.0.0.1'
user = 'root'
password = 'root'
port = 3306
db = pymysql.connect(host=host, user=user, password=password, port=port)
cursor = db.cursor()
cursor.execute("SELECT VERSION()")  # 获取版本
data = cursor.fetchone()
print("DATAVERSION:", data)
# 创建数据库
# cursor.execute("CREATE DATABASE IF NOT EXIST spiders DEFAULT CHARACTER SET utf8")
# 选择数据库
cursor.execute("USE spiders")
# 创建表
# cursor.execute("CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL ,name VARCHAR(255)"
#                "NOT NULL ,age INT NOT NULL ,PRIMARY KEY(id))")
# 插入数据
# id = 1
# name = 'ss'
# age = 12
# insert_sql1 = "INSERT INTO students(id,name,age) VALUES(%s,%s,%s)"
# try:
#     cursor.execute(insert_sql1,(id, name, age))
#     db.commit()  # 插入更新删除调用
# except Exception as e:
#     db.rollback()
# 动态插入数据
data = {
    'id': '111',
    'name': '好的',
    'age': 11
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s']*len(data))
sql = "INSERT INTO {table}({keys}) VALUES ({values})".format(table=table, keys=keys, values=values)
print(sql)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('insert success')
        db.commit()
except:
    db.rollback()
db.close()
# 更新数据库  没什么好说的

# 删除数据
condition = ""
sql = "DELETE FROM {table} WHERE {condition}".format(table=table,condition=condition)
# 查询 while + fetchone 开销小于 fetchall
cursor.fetchone()
cursor.fetchall()
#