from bs4 import BeautifulSoup

html = """
     <html>
        <head><title>标题</title></head>
        <body>
            <p class="story" name="dromouse">从前有三个小姐妹，她们的名字是
            <a href="http://example.com/elsie" class="sister" id="link1"><!--Elseie--></a>,
            <a href="http://example.com/lacie" class="sister" id="link2"><b>Lacie</b></a>,
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
            她们生活在一个井的下面</p>
            <p class="story">...</p>
        </body>
     </html>
"""
# find_all方法 传入参数   属性="..." ， name=标签名 class加_因为是关键词
soup = BeautifulSoup(html, 'lxml')
# for a in soup.find_all(name='a'):
#     print(a)
# for a in soup.find_all(class_='sister'):
#     print(a)
# 使用attrs  text匹配文本 例如 text="Lacie" 也可以传入正则表达式
# for a in soup.find_all(attrs={'class': 'sister'}):
#     print(a)
# ######################################find方法#######################################################
# 返回单个 用法同上
# print(soup.find(name="p"))
# 祖先parents  唯一父元素parent 只能先指定一个元素来进行查找 元组不行
# print(soup.find_all(name='a').find_parent(name="p"))# 这不可行
# print(soup.find(name='a').find_parent(name="p"))
# print(soup.find(name='a').find_parents())
# 前一个兄弟节点  后一个兄弟节点
print(soup.find(name='a').find_next_sibling())
print(soup.find(id='link2').find_previous_sibling())
# 前面的兄弟节点 后面的兄弟节点  返回元组
print(soup.find(name='a').find_next_siblings())
print(soup.find(id='link3').find_previous_siblings())
# 前一个元素 后一个元素
print(soup.find(name='a').find_next())
print(soup.find(id='link3').find_previous())  # 查到的是b  因为 <a><b></b></a> a->b这样的结构 在他前面是b元素
# 前面的所有元素  后面的所有元素 返回元组
print(soup.find(name='a').find_all_next())
print(soup.find(id='link3').find_all_previous())

# #######################################selectcss选择器# ################################################
# 查找class为sister的 返回的是结果元组
print(soup.select(".sister"))
print(soup.select("#link1"))  # id查询 返回的也是元组
print(soup.select("#link2 b"))  # 返回下级元素
# 嵌套查询 就是在已经查出的结果里面查询
for p in soup.select('p'):
    print(p.select('a'))
# 获取属性 attrs
for a in soup.select('a'):
    print(a.attrs['id'])
# 获取文本 get_text()
for b in soup.select('b'):
    print(b.get_text())
