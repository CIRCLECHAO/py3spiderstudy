import requests
import json
# 测试保存到json

# 读取 loads 不能用单引号 否则loads会失败 （dumps没影响）  最后一个元素不能跟逗号
str = """
    [
    {"name": "托尼", "age":2},
    {"name": "爱德华", "age":23},
    {"name": "j", "age":32}
    ]
"""
# json_str = json.loads(str)
# print(json_str)
# print(json_str[0].get('name'))
# print(json_str)
# print(type(json_str))
with open('files/export.json', 'w', encoding='utf-8') as f:
    f.write(str)
# dumps转化成字符串 +indent代表缩进字符能够存为json（没反应）  中文会变成unicode编码
with open('files/export_str.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(str, indent=2, ensure_ascii=False))