from langchain_ollama import OllamaEmbeddings


# 初始化嵌入模型对象，其默认使用模型是：text-embedding-v1
embed = OllamaEmbeddings(model = "qwen3-embedding:0.6b")

# 测试
# 注意：不用 invoke stream
# embed_query embed_documents
print(embed.embed_query("你好"))  # 结果是一个列表（向量）
print(embed.embed_query("我爱你"))   # 单次转换
print(embed.embed_documents(["i love you", "我爱你"])) # 批量转换