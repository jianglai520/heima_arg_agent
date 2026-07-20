# jq是一个跨平台的json解析工具，langchain底层对json的解析就是基于jq工具实现的
from langchain_community.document_loaders import JSONLoader

# loader = JSONLoader(
#     file_path = "./data/stu.json",   # 文件路径
#     jq_schema = ".",  # jq schema语法
#     text_content = False,   # 抽取的是否是字符串,默认True(默认是字符串)
#     # json_lines = True,  # 是否是JsonLines文件
# )
#
#
# document = loader.load()
# print(document)

# loader = JSONLoader(
#     file_path = "./data/stus.json",
#     jq_schema = ".[].name",
#     text_content = False
# )
#
# document = loader.load()
# print(document)


loader = JSONLoader(
    file_path = "./data/stu_json_lines.json",
    jq_schema = ".",
    text_content = False,
    json_lines = True    # 告知JSONLoader 这是一个JSONLines文件
)

document = loader.load()
print(document)

