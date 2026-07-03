from langchain_ollama import OllamaLLM

model = OllamaLLM(model="deepseek-r1:8b")


# invoke一次性返回结果
res = model.invoke(input = "请写一个关于机器学习的段落")
print(res)