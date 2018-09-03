import csv


with open('files/data.csv', 'w', ) as csv_file:
    writer = csv.writer(csv_file, delimiter=" ")  # 分隔符 默认是英文逗号
    # 写入单行
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['1', 'w', 21])
    writer.writerow(['2', 'e', 32])
    writer.writerow(['3', 'for t', 23])
    writer.writerow(['4', 't', 1])
    # 写入多行 传入二维列表
    writer.writerows([['4', 't', 1], ['4', 't', 2], ['4', 't', 3]])

# 字典的方式写入
with open('files/data_dic.csv', 'w', encoding='utf-8') as csv_file:  # encoding中文乱码处理
    field_names = ['id', 'name', 'age']  # 初始化写入字典的结构 使用dictwriter
    writer = csv.DictWriter(csv_file, delimiter=" ", fieldnames=field_names)  # 分隔符 默认是英文逗号
    # 写入标题
    writer.writeheader()
    # 写入单行
    writer.writerow({'id': '1', 'name': '的', 'age': 2})
    writer.writerow({'id': '1', 'name': '啊', 'age': 2})
    writer.writerow({'id': '1', 'name': '的', 'age': 2})
    writer.writerow({'id': '1', 'name': '飞', 'age': 2})
    # 写入多行 传入字典元组
    writer.writerows([{'id': '1', 'name': 'tony', 'age': 2}, {'id': '1', 'name': 'tony', 'age': 2},
                      {'id': '1', 'name': 'tony', 'age': 2}])

# 读取csv  读取元组和字典都是可以的 读出来都是数组
with open('files/data_dic.csv', 'r', encoding='utf-8') as csv_file:  # encoding中文乱码处理
    reader = csv.reader(csv_file)
    for row in reader:
        if row != []:
            print(row)

# 读取csv  读取元组和字典都是可以的 读取的是OrderedDict对象
with open('files/data.csv', 'r', encoding='utf-8') as csv_file:  # encoding中文乱码处理
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)

