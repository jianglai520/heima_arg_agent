# 组成的链在执行上有：上一个组件的输出作为下一个组件的输入的特性
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi


chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个边塞诗人，可以作诗"),
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

model = ChatTongyi(model = "qwen3.7-max")

# 组成chain,每一个组件都是runnable接口的子类
chain = chat_prompt_template | model


# 通过链去调用invoke或stream
# res = chain.invoke(input = {"histoty":history_data})
# print(res.content)

# 通过流式输出
for chunk in chain.stream(input = {"history":history_data}):
    print(chunk.content, end = "", flush = True)


