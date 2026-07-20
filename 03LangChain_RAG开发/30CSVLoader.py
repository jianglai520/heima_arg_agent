from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path = "./data/stu.csv",
    csv_args = {
        "delimiter":",",   # 指定分隔符
        "quotechar":'"',  # 指定带有分隔符文本的引号包围是单引号还是双引号
        "fieldnames": ['name', 'age', 'gender', 'hobby']   # 如果数据没有表头就可以用
    },
    encoding = "utf-8"   # 指定编码
)

# 批量加载 .load() -> [Document, Document, ...]
# documents = loader.load()
#
# print(documents)
# for i in documents:
#     print(type(i), i)

# 懒加载：.lazy_load()  迭代器[Document]
for i in loader.lazy_load():
    print(i)