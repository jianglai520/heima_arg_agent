from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了{gender},你帮我起名字，好听一点。"
)

# # 调用.format方法注入信息即可
# prompt_text = prompt_template.format(lastname = "张", gender = "男孩儿")
# # print(prompt_text)
#
# model = OllamaLLM(model = "deepseek-r1:1.5b")
# res = model.invoke(input = prompt_text)
# print(res)

# 注意：大语言模型和对话模型都可以，自己选择
model = OllamaLLM(model = "deepseek-r1:1.5b")

chain = prompt_template | model   # 提示词模板和模型组成链条
res = chain.invoke(input = {"lastname": "张", "gender": "女儿"})

print(res)