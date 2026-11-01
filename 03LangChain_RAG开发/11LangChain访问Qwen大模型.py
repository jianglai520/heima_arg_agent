from langchain_community.llms.tongyi import Tongyi

# qwen-max是大语言模型 -- 最新测试免费额度已耗尽
model = Tongyi(model = "qwen-max")

# 调用invoke向模型提问
res = model.invoke(input = "请写一个关于机器学习的段落")
print(res)
