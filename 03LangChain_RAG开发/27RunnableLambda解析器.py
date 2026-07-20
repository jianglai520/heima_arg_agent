from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi


model = ChatTongyi(model = "qwen3.7-max", streaming = True)
str_parser = StrOutputParser()

first_prompt = PromptTemplate.from_template(
    "我叫：{lastname}, 刚生了{gender}, 请起名,仅告知我一个名字，不需要额外信息。"
)

second_prompt = PromptTemplate.from_template(
    "姓名{name},请帮我解析含义。"
)

# 函数的入参：AIMessage -> dict({"name":XXX})
my_func = RunnableLambda(lambda ai_msg: {"name": ai_msg.content})

chain = first_prompt | model | my_func | second_prompt | model | str_parser

for chunk in chain.stream({"lastname": "张", "gender": "男孩儿"}):
    print(chunk, end = "", flush = True)