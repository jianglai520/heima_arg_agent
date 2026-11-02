from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import ChatOllama

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个唐朝诗人，可以作诗"),
        MessagesPlaceholder("history"),
        ("human", "请再来一首唐诗"),

    ]
)

history_data = [
    ("human", "请来一首唐诗"),
    ("ai", "风急天高猿啸哀，渚清沙白鸟飞回"),
    ("human", "好诗好诗，再来一首"),
    ("ai","春风得以马蹄疾，一日看尽长安花"),
]

# StringPromptValue
# 注意：必须是invoke，format无法注入
prompt_text = chat_prompt_template.invoke(input = {"history":history_data}).to_string()
print(prompt_text)
# print(type(prompt_text))

model = ChatOllama(model = "deepseek-r1:1.5b")  # 调用ollama本地模型
res = model.invoke(input = prompt_text)
print(res.content)
print(type(res))