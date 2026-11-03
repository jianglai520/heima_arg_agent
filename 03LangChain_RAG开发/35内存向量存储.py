from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import CSVLoader

vector_store = InMemoryVectorStore(
    embedding = OllamaEmbeddings(model = "qwen3-embedding:0.6b")  # 调用本地ollama文本嵌入模型
)

loader = CSVLoader(
    file_path = "./data/info.csv",
    encoding = "utf-8",
    source_column = "source",    # 指定本条数据来源是哪里
)

documents = loader.load()

# print(documents)


# 向量存储的新增、删除、检索
vector_store.add_documents(
    documents = documents,   # 被添加的文档，类型：list[Document] （列表套Document对象）
    ids = ["id" + str(i) for i in range(1, len(documents) + 1)]       # 给添加的吻搭档提供id(字符串) list[str]
)


# 删除 传入[id, id...]
vector_store.delete(
    ["id1", "id2"]
)


# 检索（相似度搜索） -- 返回类型 list[Document]
result = vector_store.similarity_search(
    "Python是不是简单易学呀",
    3    # 检索的结果要几个
)

print(result)