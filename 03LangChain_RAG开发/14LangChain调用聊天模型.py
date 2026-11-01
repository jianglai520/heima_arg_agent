from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv(override = True)

# 初始化模型(用聊天模型)
chat = ChatOpenAI(
    model = "qwen3.8-flash",
    api_key = os.getenv("DASHSCOPE_API_KEY"),   # 明确传入阿里云 key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 指向阿里云兼容端点
)

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