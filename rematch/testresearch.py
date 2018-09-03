import re
# content = 'Hello 1234567 World_This is a regex demo'
# result = re.search('1.*\d+.*7', content)
# result1 = re.match('1.*\d+.*7', content)  # 必须从开始匹配
# print(result)
# print(result1)

html = """
<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">经典老歌列表</p>
    <ul  id =" list " class =" list-group ">
        <li data-view="2">
            一路上有你
        </li>
        <li  data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一卢笑</a>
        </li>
        <li data-view ="4" class ="active">
            <a href = "/3.mp3" singer="齐泰">往事随风</a>
        </li>
        <li data-view="6">
            <a href = "/4.mp3" singer ="beyond">尤辉岁月</a> 
        </li>
        <li data-view ="5">
            <a href = "/S.mp3"singer="陈慧琳">记事本</a> 
        </li>
        <li  data-view ="5">
            <a href = "/6.mp3"singer="邓丽君">但愿人长久</a>
        </li>
        </ul>
</div>
"""
# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
# if result:
#     print(result.group(1), result.group(2))

# results = re.findall('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)

# results = re.findall('<a href="(.*?)"singer="(.*?)">(.*?)</a>', html, re.S)
# if results:
#     for result in results:
#         print(result)

# 替换函数sub
# word = "asd23asd324ed32e3e32e32"
# word = re.sub("\d", "GOOD", word)
# print(word)

# compile 生成匹配正则条件
content = '2012-02-13 12:12 2012-02-13 12:04 2012-02-13 22:12'
pattern = re.compile('\d{2}:\d{2}')  # 匹配出日期 两个数字：两个数字

print(re.sub(pattern, "", content))  # 替换掉匹配到的内容