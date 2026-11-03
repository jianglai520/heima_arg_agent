# 文档分割器 RecursiveCharacterTextSplitter(按照自然段落分割大文档)
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


loader = TextLoader(
    "./data/Python基础语法.txt",
    encoding = "utf-8"
)

docs = loader.load()

# print(docs)
# print(len(docs))
# print(type(docs))

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,    # 分段的最大字符数
    chunk_overlap = 50,  # 分段之间允许重叠字符数
    separators = ["\n\n", "\n", "。", "！","?"," ", "", '.'],  # 分隔符（分段依据）
    length_function = len,    # 统计字符的依据函数
)

split_docs = splitter.split_documents(docs)
# print(type(split_docs))
print(len(split_docs))
for doc in split_docs:
    print("=" * 20)
    print(doc)
    print("=" * 20)