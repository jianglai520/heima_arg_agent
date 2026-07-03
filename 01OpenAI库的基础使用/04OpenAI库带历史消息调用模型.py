from openai import OpenAI

# 1.获取client对象，OpenAI类对象
client = OpenAI(
    base_url = "https://ws-3ssufixwbthuxno3.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)


# 2.调用模型
response = client.chat.completions.create(
    model = "qwen3.7-max",
    messages = [
        {"role":"system", "content":"你是一个AI助理，回答问题简洁"},
        {"role":"user", "content":"小明有两只狗"},
        {"role":"assistant", "content":"好的，小明有2只狗"},
        {"role":"user", "content":"小红有三只猫"},
        {"role":"assistant", "content":"好的，小红有3只猫"},
        {"role":"user", "content":"小明和小红一共有多少只动物"}
    ],
    stream = True    # 开启流式输出
)


# 3.处理结果
# print(response.choices[0].message.content)
for chunk in response:
    # 检查choices列表是否为空，以及delta对象是否为空(是否有content)
    if chunk.choices and len(chunk.choices) > 0:
        delta = chunk.choices[0].delta
        if delta.content:    # 检查content是否为None
            print(
                delta.content,
                end="",
                flush=True)    # 立即刷新缓冲区