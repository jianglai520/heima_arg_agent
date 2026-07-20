# StrOutputParser 是 LangChain内置的简单字符串解析器，可以将AIMessage转换为普通字符串
from langchain_core.messages import AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate


parser = StrOutputParser()
model = ChatTongyi(model = "qwen3.7-max")
prompt = PromptTemplate.from_template(
    "我叫：{lastname}, 刚生了{gender}, 请起名， 仅告知我名字无需其他多余内容"
)

chain = prompt | model | parser | model

res: AIMessage = chain.invoke({"lastname": "张", "gender": "男孩儿"})
print(res.content)
print(type(res))
