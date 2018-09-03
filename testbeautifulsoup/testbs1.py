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
soup = BeautifulSoup(html, 'lxml')
# 格式化输出
# print(soup.prettify())
# 打印title节点的内容
# print(soup.title.string)
# 选择元素 会获取到第一个匹配到的该元素
# print(soup.head)
# print(soup.p)
# 获取元素的属性 若不是唯一属性 例如 name id  则通过attrs获取
# print(soup.title.name)
# print(soup.a.attrs)
# print(soup.a.attrs['class'])
# print(soup.a.attrs['href'])
# 关联选择 如 父子 兄弟等
# print(soup.p.contents)
# 子节点 不拆分子孙节点
# print(soup.p.children)
# for i, child in enumerate(soup.p.children):
#     print(i, child)
# 子孙节点 全部查询出来
# print(soup.p.descendants)
# for i, child in enumerate(soup.p.descendants):
#     print(i, child)
# parent 唯一父元素
print(soup.a.parent)

# parents 祖先元素 p  body  html 一层一层往上
print(soup.a.parents)
for i, child in enumerate(soup.a.parents):
    print(i, child)