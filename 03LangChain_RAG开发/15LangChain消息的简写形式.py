# 简写形式可以避免导包、写起来更简单，可在运行时填充具体值
from langchain_ollama import ChatOllama

# 初始化模型(用聊天模型)
chat = ChatOllama(model = "deepseek-r1:8b")

# 准备消息list
messages = [
    # 是动态的，需要在运行时，由langchain内部机制转换为Message类对象
    ("system", "你是一个边塞诗人"),  # 元组形式，无需导包（角色，内容）
    ("human", "写一首唐诗"),
    ("ai", "锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦"),
    ("human", "按照你上一个回复的格式，再写一首唐诗")
]


# 调用stream流式输出
res = chat.stream(input = messages)
for chunk in res:
    print(chunk.content, end = "", flush = True)