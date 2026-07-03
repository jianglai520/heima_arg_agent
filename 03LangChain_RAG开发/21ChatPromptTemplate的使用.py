from langchain_classic.chains.question_answering.refine_prompts import chat_qa_prompt_template
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi


chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个边塞诗人，可以作诗"),
        MessagesPlaceholder("histoty"),
        ("human", "请再来一首唐诗"),

    ]
)

history_data = [
    ("human", "请来一首唐诗"),
    ("ai", "风急天高猿啸哀，渚清沙白鸟飞回"),
    ("human", "好诗好诗，再来一首"),
    ("ai","春风得以马蹄疾，一日看尽长安花"),
]


# StringPromptTemplate
prompt_text = chat_prompt_template.invoke(input = {"histoty":history_data}).to_string()
# print(prompt_text)

model = ChatTongyi(model = "qwen3.7-max")
res = model.invoke(input = prompt_text)
print(res.content, type(res))