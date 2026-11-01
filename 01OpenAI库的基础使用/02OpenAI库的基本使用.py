from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(override = True)

# 1.获取client对象，OpenAI类对象
client = OpenAI(
    # base_url = "https://ws-3ssufixwbthuxno3.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"

    # 调用deepseek大模型
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL")
)

# 2.调用模型
response = client.chat.completions.create(
    # model = "qwen3.7-max",
    model = "deepseek-flash",
    messages = [
        {"role":"system", "content":"你是一个python专家，回答问题简明扼要"},
        {"role":"assistant", "content":"好的，我是编程专家，并且回答问题简明扼要"},
        {"role":"user", "content":"输出1-10的数字，用python代码"}
    ]   # 列表里面嵌套字典
)

# 3.处理结果
print(response)
print(response.choices[0].message.content)