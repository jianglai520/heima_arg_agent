from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate, ChatPromptTemplate


"""
PromptTemplate -> StringPromptTemplate -> BasePromptTemplate -> RunnableSerializable -> Runnable
FewShotPromptTemplate -> StringPromptTemplate -> BasePromptTemplate -> RunnableSerializable -> Runnable
ChatPromptTemplate -> BaseChatPromptTemplate -> BasePromptTemplate -> RunnableSerializable -> Runnable
"""

template = PromptTemplate.from_template("我的邻居姓{lastname},刚生了{gender},你帮我起名字，简单回答。")


# format得到的是字符串
res = template.format(lastname = "张", gender = "男孩儿")
print(res, type(res))

# invoke得到的是PromptValue类对象
res1 = template.invoke({"lastname": "王", "gender": "女孩儿"})
print(res1, type(res1))
