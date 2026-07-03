from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

prompt = PromptTemplate.from_template("{input}")
model = Tongyi(model = "qwen-max")

chain = prompt | model | prompt | model
print(type(chain))     # <class 'langchain_core.runnables.base.RunnableSequence'>