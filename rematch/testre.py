import re
content = 'Hello 1234567 World_This is a regex demo'
content1 = """Hello 1234567 World_This 
is a regex demo"""
# result = re.match('^Hello\s(\d+)\sWorld', content)
# result = re.match('^.*$', content)
# result = re.match('^He.*(\d+).*demo$', content) # 贪婪匹配只有7 .*将前面的匹配完了 \d=只匹配到一个7
result = re.match('^He.*?(\d+).*demo$', content)  # 非贪婪匹配
result1 = re.match('^He.*?(\d+).*demo$', content1, re.S)  # 非贪婪匹配  S使得换行符被匹配

# print(result)
# print(result.group())
# print(result.group(1)) # 贪婪匹配只有7 .*将前面的匹配完了 \d=只匹配到一个7
# print(result.span()

print(result1)
print(result1.group())
print(result1.group(1))  # 贪婪匹配只有7 .*将前面的匹配完了 \d=只匹配到一个7
print(result1.span())