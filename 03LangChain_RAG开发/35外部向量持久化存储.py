# 外部向量持久化存储
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

# Chroma 向量数据库（轻量级的）
# 确保 langchain-chroma chromadb 这两个库要安装

vector_store = Chroma(
    collection_name = "test",   # 当前向量存储起个名字，类似数据库的表名称
    embedding_function = DashScopeEmbeddings(),    # 提供嵌入模型
    persist_directory = "./chroma_db"    # 指定数据存放的文件夹
)

# vector_store = InMemoryVectorStore(
#     embedding = DashScopeEmbeddings()
# )

loader = CSVLoader(
    file_path = "./data/info.csv",
    encoding = "utf-8",
    source_column = "source",    # 指定本条数据来源是哪里
)

documents = loader.load()

# print(documents[1])


# 向量存储的新增、删除、检索
vector_store.add_documents(
    documents = documents,   # 被添加的文档，类型：list[Document]
    ids = ["id" + str(i) for i in range(1, len(documents) + 1)]             # 给添加的吻搭档提供id(字符串) list[str]
)


# 删除 传入[id, id...]
vector_store.delete(
    ["id1", "id2"]
)


# 检索(相似度搜索)
result = vector_store.similarity_search(
    "Python是不是简单易学呀",
    3,   # 检索结果的数量
    filter = {"source":"黑马程序员"}
)
print(result)

