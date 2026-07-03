# from langchain_community.llms.tongyi import Tongyi
#
# model = Tongyi(model = "qwen-max")
#
#
# # stream方法获得流式输出
# res = model.stream(input = "请写一个关于机器学习的段落")
#
# for chunk in res:
#     print(chunk, end = "", flush = True)   # flush = True 保证输出


from langchain_ollama import OllamaLLM

model = OllamaLLM(model="deepseek-r1:8b")

res = model.stream(input = "请写一个关于机器学习的段落")

for chunk in res:
    print(chunk, end = "", flush = True)