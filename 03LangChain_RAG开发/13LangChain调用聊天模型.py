from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


# 初始化模型(用聊天模型)
chat = ChatTongyi(model = "qwen3-max")

# 准备消息list
messages = [
    SystemMessage(content = "你是一个边塞"),
    HumanMessage(content = "写一首诗"),
    AIMessage(content = "春风得意马蹄疾，一日看尽长安花"),
    HumanMessage(content = "按照上面这两句，写两句唐诗")
]


# 调用stream流式输出
res = chat.stream(input = messages)
for chunk in res:
    print(chunk.content, end = "", flush = True)