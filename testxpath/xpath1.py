from lxml import etree
text = """
<div>
<ul>
<li class="item-0"><a href="link1,html">one</a></li>
<li class="item-1"><a href="link1,html">two</a></li>
<li class="item-inactive"><a href="link1,html">three</a></li>
<li class="item-1"><a href="link1,html">four</a></li>
<li class="item-0"><a href="link1,html">five</a>
</ul>
</div>
"""
html = etree.HTML(text)
# 从文本读取
html = etree.parse('test.html', etree.HTMLParser())
result = etree.tostring(html)  # bytes类型
# print(result)
# print(result.decode('utf-8'))  # string类型

#匹配
# rp1 = html.xpath('//*')
# print(rp1)

# rp2 = html.xpath('//li')
# print(rp2)

# 匹配文本
rp3 = html.xpath("//li[@class='item-0']/a/text()")
print(rp3)
rp4 = html.xpath("//li[@class='item-0']//text()")
print(rp4)
# 获取属性
rp5 = html.xpath('//li//a/@href')
print(rp5)

# 一个属性多个值 需要contains匹配
rp6 = html.xpath("//li[contains(@class, '-first')]/a/text()")
print(rp6)

# 多属性匹配 and连接
rp7 = html.xpath("//li[contains(@class, 'li') and @name='item']//text()")
print(rp7)
# 在条件中传入顺序 如数字 position()> last等等
rp8 = html.xpath("//li[1]/a/text()")
rp9 = html.xpath("//li[position()>2]/a/text()")
rp10 = html.xpath("//li[last()-1]/a/text()")
print(rp8)
print(rp9)
print(rp10)