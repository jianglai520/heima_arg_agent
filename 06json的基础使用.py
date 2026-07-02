import json

# 1.python 对象转 json字符串
# python字典
d = {
    "name": "小明",
    "age": 18,
    "sex": "男"
}

dd = json.dumps(d, ensure_ascii = False)    # ensure_ascii = False 避免中文乱码
print(dd)   # 标准的json格式都是双引号

# python列表
ll = [
{
    "name": "小明",
    "age": 18,
    "sex": "男"
     },
{
    "name": "小刚",
    "age": 19,
    "sex": "男"
     },
{
    "name": "小圆",
    "age": 20,
    "sex": "女"
     },
{
    "name": "小光",
    "age": 12,
    "sex": "男"
     },

]
print(json.dumps(ll, ensure_ascii=False))


# 2.json字符串转换为python对象
json_str = '{"name": "小明", "age": 18, "sex": "男"}'
json_array_str = '[{"name": "小明", "age": 18, "sex": "男"}, {"name": "小刚", "age": 19, "sex": "男"}, {"name": "小圆", "age": 20, "sex": "女"}, {"name": "小光", "age": 12, "sex": "男"}]'

res_dict = json.loads(json_str)
print(res_dict, type(res_dict))

res_list = json.loads(json_array_str)
print(res_list, type(res_list))














