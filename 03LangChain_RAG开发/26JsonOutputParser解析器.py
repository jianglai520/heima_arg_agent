from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate

# 创建所需的解析器
str_parser = StrOutputParser()
json_parser = JsonOutputParser()

# 创建所需的模型
model = ChatTongyi(model = "qwen3.7-max", streaming = True)   # streaming = True 实现流式输出


# 第一个提示词模板
first_prompt = PromptTemplate.from_template(
    "我叫：{lastname}, 刚生了{gender}, 请起名，并封装为json格式返回给我，key是name, value就是你起的名字，请严格遵守要求"
)

# 第二个提示词模板
second_prompt = PromptTemplate.from_template(
    "姓名:{name}, 请帮我解析含义。"
)

# 创建链 AIMessage("{name:XXX}")
chain = first_prompt | model | json_parser | second_prompt | model | str_parser

for chunk in chain.stream({"lastname": "张", "gender": "男孩儿"}):
    print(chunk, end = "", flush = True)


