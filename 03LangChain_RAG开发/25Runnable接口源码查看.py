from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

prompt = PromptTemplate.from_template("你是一个AI助手")
model = OllamaLLM(model = "deepseek-r1:1.5b")

chain = prompt | model | prompt | model
print(type(chain))     # <class 'langchain_core.runnables.base.RunnableSequence'>