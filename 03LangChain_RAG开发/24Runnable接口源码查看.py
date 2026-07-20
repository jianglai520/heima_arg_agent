from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

prompt = PromptTemplate.from_template("你是一个AI助手")
model = Tongyi(model = "qwen-max")

chain = prompt | model | prompt | model
print(type(chain))     # <class 'langchain_core.runnables.base.RunnableSequence'>