from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_ollama import OllamaLLM

# 示例的模板
example_template = PromptTemplate.from_template(
    "单词:{word}, 反义词：{antonym}"
)

# 示例的动态数据注入, 要求list套dict
examples_data = [
    {"word":"大", "antonym":"小"},
    {"word":"上", "antonym":"下"},
    {"word":"美", "antonym":"丑"}
]

# FewShotPromptTemplate类对象构建需要5个核心参数
few_shot_template = FewShotPromptTemplate(
    example_prompt=example_template,  # 示例数据的模板
    examples = examples_data,    # 示例的数据
    prefix = "告知我单词的反义词，我提供如下的示例",   # 示例之前的提示词
    suffix = "基于前面的示例告知我{input_word}的反义词是?",    # 示例之后的提示词
    input_variables = ['input_word']    # 声明在前缀或后缀中需要注入的变量名
)

prompt_text = few_shot_template.invoke(input = {"input_word":"左"}).to_string()  # to_string() 转成字符串输出
# print(prompt_text)

model = OllamaLLM(model = "deepseek-r1:1.5b")
print(model.invoke(input=prompt_text))