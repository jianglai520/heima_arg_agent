from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(override = True)  # 强制让 .env 文件里的变量值覆盖系统中已存在的同名环境变量。

# 1.获取client对象，OpenAI类对象
client = OpenAI(
    # base_url = "https://ws-3ssufixwbthuxno3.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"

    # 调用deepseek大模型
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL")
)


# 2.调用模型
response = client.chat.completions.create(
    model = "deepseek-flash",
    messages = [
        {"role":"system", "content":"你是一个python专家，回答问题详细"},
        {"role":"assistant", "content":"好的，我是编程专家，并且回答问题详细"},
        {"role":"user", "content":"输出1-10的数字，用python代码"}
    ],
    stream = True    # 开启流式输出 -- 必要的字段否则报错
)


# 3.处理结果
# print(response.choices[0].message.content)
for chunk in response:
    # print(
    #     chunk.choices[0].delta.content,
    #     end = "",
    #     flush = True    # 立刻刷新缓冲区
    # )


    # 注意，流式输出时，如果chunk.choice[0].delta.content为None，就会输出None,可以通过if content 去除None
    content = chunk.choices[0].delta.content
    if content:
        print(content, end = "", flush = True)