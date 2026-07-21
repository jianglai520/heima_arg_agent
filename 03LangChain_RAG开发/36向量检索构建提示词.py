"""
提示词：用户的提问 + 向量库中检索到的参考资料
"""

from langchain_community.chat_models import ChatTongyi
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import  ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatTongyi(model = "qwen3.7-max")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","以我提供的已知参考资料为主，简洁和专业的回答用户问题，参考资料：{content}。"),
        ("user","用户提问：{input}")
    ]
)

vector_store = InMemoryVectorStore(embedding = DashScopeEmbeddings(model = "text-embedding-v4"))

# 准备一下资料（向量数据库）
# add_texts() 传入一个list[str]
vector_store.add_texts(["减肥就是要少吃多练", "在减脂期间吃东西很重要，清淡少油控制卡路里摄入并运行起来", "跑步是很好的运动哦"])


input_text = "如何减肥"

# 检索向量库
result = vector_store.similarity_search(input_text, 2)
# print(result)

reference_text = "["
for doc in result:
    reference_text += doc.page_content
reference_text += "]"

# print(reference_text)


def print_prompt(prompt):
    print(prompt.to_string)
    print("="*20)
    return prompt

# 链
chain = prompt | print_prompt | model | StrOutputParser()

res = chain.invoke({"input":input_text, "content":reference_text})
print(res)

