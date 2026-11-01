from openai import OpenAI

# 1.获取client对象，OpenAI类对象
client = OpenAI(
    base_url = "http://localhost:11434/v1"
)

# 2.调用模型
response = client.chat.completions.create(
    model = "deepseek-r1:1.5b",   # 下载好的本地模型
    messages = [
        {"role":"system", "content":"你是一个python专家，回答问题简明扼要"},
        {"role":"assistant", "content":"好的，我是编程专家，并且回答问题简明扼要"},
        {"role":"user", "content":"给我详细讲解拓扑排序算法并给出两种语言的算法实现代码"}
    ],
    stream = True  # 流式输出
)


# 3.处理结果
# print(response)
# print(response.choices[0].message.content) # 非流式输出

# 流式输出
for chunk in response:
    print(chunk.choices[0].delta.content, end="", flush=True)