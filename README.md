# 🤖 Heima RAG Agent — 黑马 RAG 智能体开发实战教程

> 一个循序渐进的大模型 RAG（检索增强生成）智能体开发学习项目，基于 Python + OpenAI 兼容接口 + LangChain 框架构建。
>
> 项目来源：**黑马程序员** 大模型开发课程配套代码

---

## 📋 项目概述

本项目是**从零入门大模型应用开发**的完整实战教程，分为三个逐步递进的学习阶段：

| 阶段 | 模块 | 内容 | 文件数 |
|------|------|------|--------|
| 1️⃣ | OpenAI 库的基础使用 | 调用大模型 API 的基础能力 | 4 |
| 2️⃣ | 提示词优化 | Prompt Engineering 实战 | 4 |
| 3️⃣ | LangChain RAG 开发 | 完整 RAG 流水线构建 | 29+ |

涵盖的技术栈包括：**OpenAI SDK、阿里云百炼（通义千问）、Ollama 本地模型（DeepSeek、Qwen）、LangChain 框架、Chroma 向量数据库、文本嵌入、提示词模板、文档加载器、会话记忆** 等。

---

## 📂 项目结构

```
E:/heima_rag_agent/
├── 01OpenAI库的基础使用/           # 第一阶段：OpenAI SDK 入门
│   ├── 01测试api_key使用.py         # 测试 API Key 连接（阿里云百炼 + Ollama）
│   ├── 02OpenAI库的基本使用.py      # OpenAI SDK 基本调用（system/assistant/user 角色）
│   ├── 03OpenAI库的流式输出.py      # Streaming 流式输出
│   └── 04OpenAI库带历史消息调用模型.py # 多轮对话历史消息传递
│
├── 02提示词优化/                   # 第二阶段：提示词工程
│   ├── 05提示词优化案例——金融文本分类.py   # Few-shot 金融文本分类
│   ├── 06json的基础使用.py                 # JSON 序列化/反序列化
│   ├── 07提示词优化案例——金融信息抽取.py    # Few-shot 金融信息抽取（输出 JSON）
│   └── 08提示词优化——金融文本匹配判断.py    # 文本语义匹配判断
│
├── 03LangChain_RAG开发/            # 第三阶段：LangChain + RAG 完整开发
│   ├── 09余弦相似度.py                     # 向量余弦相似度手动实现
│   ├── 10LangChain访问Qwen大模型.py        # LangChain + 通义千问
│   ├── 11LangChain访问Ollama本地模型.py    # LangChain + Ollama 本地模型
│   ├── 12LangChain流式输出.py              # LangChain 流式输出
│   ├── 13LangChain调用聊天模型.py          # Chat Model（聊天模型）
│   ├── 14LangChain调用本地ollama聊天模型.py # Ollama 聊天模型
│   ├── 15LangChain消息的简写形式.py        # 消息元组简写 (role, content)
│   ├── 16LangChain文本嵌入模型使用.py       # DashScope 文本嵌入
│   ├── 17LangChain文本嵌入模型使用(ollama).py # Ollama 本地嵌入模型
│   ├── 18通用提示词模板.py                 # PromptTemplate 基础
│   ├── 19fewshot提示词模板.py              # FewShotPromptTemplate
│   ├── 20模板类的format和invoke方法.py      # format() vs invoke()
│   ├── 21ChatPromptTemplate的使用.py       # 聊天提示词模板 + MessagesPlaceholder
│   ├── 22LangChain中chain链的学习.py       # 链式调用（`|` 管道符）
│   ├── 23[扩展]python的或运算符的重写.py   # Python `__or__` 魔术方法原理
│   ├── 24Runnable接口源码查看.py           # Runnable 接口与 RunnableSequence
│   ├── 25StrOutputParser解析器.py          # 字符串输出解析器
│   ├── 26JsonOutputParser解析器.py         # JSON 输出解析器
│   ├── 27RunnableLambda解析器.py           # 自定义 Lambda 解析器
│   ├── 28临时会话记忆.py                   # InMemoryChatMessageHistory 临时记忆
│   ├── 29长期会话记忆.py                   # FileChatMessageHistory 文件持久化记忆
│   ├── 30CSVLoader.py                      # CSV 文档加载器
│   ├── 31JSONLoader.py                     # JSON/JSONLines 文档加载器
│   ├── 32TextLoader.py                     # 文本加载器 + RecursiveCharacterTextSplitter
│   ├── 33PDFLoader.py                      # PyPDFLoader PDF 加载器
│   ├── 34内存向量存储.py                   # InMemoryVectorStore 向量检索
│   ├── 35外部向量持久化存储.py             # Chroma 持久化向量数据库
│   ├── 36向量检索构建提示词.py             # 向量检索 + RAG 提示词构建
│   ├── 37RunnablePassThrough使用.py        # RunnablePassthrough RAG 流水线
│   ├── data/                               # 示例数据文件
│   │   ├── info.csv                        # 信息类 CSV 数据（黑马/传智）
│   │   ├── stu.csv                         # 学生 CSV 数据
│   │   ├── stu.json                        # JSON 数据
│   │   ├── stus.json                       # JSON 数组数据
│   │   ├── stu_json_lines.json             # JSONLines 数据
│   │   ├── Python基础语法.txt              # Python 语法参考文档
│   │   ├── pdf1.pdf                        # PDF 文件 1
│   │   └── pdf2.pdf                        # PDF 文件 2（密码保护）
│   ├── chroma_db/                          # Chroma 向量数据库持久化目录
│   ├── chat_history/                       # 长期会话记忆存储文件
│   └── 管道符理解                          # Python `|` 管道符执行流程笔记
│
└── README.md                              # 本文件
```

---

## 🔧 环境要求

### 1. Python 版本
- Python 3.8+

### 2. 依赖安装

```bash
# 核心依赖
pip install openai langchain langchain-community langchain-ollama langchain-chroma
pip install chromadb numpy pypdf jq
```

### 3. 模型服务配置

项目支持两种模型服务方式：

#### 方式一：阿里云百炼（通义千问）

在代码中配置 `base_url` 和 `api_key`：

```python
from openai import OpenAI
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="sk-xxx"  # 替换为你的阿里云百炼 API Key
)
```

#### 方式二：Ollama 本地模型

安装 [Ollama](https://ollama.com/) 后拉取模型：

```bash
ollama pull deepseek-r1:8b
ollama pull qwen3-embedding:0.6b
```

```python
client = OpenAI(
    base_url="http://localhost:11434/v1"
)
```

> 部分文件默认指向阿里云百炼，部分指向 Ollama，可互相替换。
> 所有文件均保留了对应的注释说明。

---

## 📖 模块详解

### 阶段 1：OpenAI 库的基础使用

学习通过 OpenAI 兼容 SDK 调用大模型 API 的基本操作。

| 文件 | 学习要点 |
|------|---------|
| `01` | 测试 API Key 连通性；流式解析 `reasoning_content` 与 `content`（支持 DeepSeek 思考过程） |
| `02` | 完整调用流程：创建 Client → 构建 messages → 调用模型 → 处理响应；角色体系（system/assistant/user） |
| `03` | `stream=True` 流式输出，逐块打印响应内容 |
| `04` | 多轮对话历史维护，让模型基于上下文回答 |

**关键概念：**
- `messages` 列表结构：`system`（系统指令）、`assistant`（助手回复）、`user`（用户输入）
- 流式输出与普通输出的区别与适用场景

---

### 阶段 2：提示词优化

学习 Few-shot Prompt Engineering 技巧，应用于金融领域的文本任务。

| 文件 | 学习要点 |
|------|---------|
| `05` | **金融文本分类**：Few-shot 示例引导模型将文本分类为「新闻报道/财务报道/公司公告/分析师报告」 |
| `06` | **JSON 基础**：Python JSON 序列化与反序列化（为后续结构化输出做准备） |
| `07` | **金融信息抽取**：Few-shot 指导模型从金融文本中抽取「日期/股票名称/开盘价/收盘价/成交量」等结构化信息，以 JSON 格式输出 |
| `08` | **文本匹配判断**：判断两个金融文本是否语义匹配（「是/不是」二分类） |

**关键概念：**
- **Few-shot Learning**：在 prompt 中提供输入-输出示例，引导模型理解任务
- **结构化输出**：要求模型以 JSON 格式返回结果，便于程序解析
- **金融场景**：文本分类、信息抽取、语义匹配三个典型 NLP 任务

---

### 阶段 3：LangChain RAG 开发

使用 LangChain 框架构建完整 RAG 流水线，是本项目的核心模块。

#### 子模块 A：模型接入（09-17）

| 文件 | 学习要点 |
|------|---------|
| `09` | 余弦相似度手动实现（向量检索的数学基础） |
| `10` | `LangChain + Tongyi`：通过 `langchain_community.llms.tongyi` 调用通义千问 |
| `11` | `LangChain + Ollama`：通过 `langchain_ollama.OllamaLLM` 调用本地模型 |
| `12` | LangChain 流式输出（`model.stream()`） |
| `13` | 聊天模型 `ChatTongyi` + `HumanMessage/SystemMessage/AIMessage` |
| `14` | Ollama 聊天模型 `ChatOllama` |
| `15` | 消息简写：`("human", "内容")` 元组形式代替类对象 |
| `16` | `DashScopeEmbeddings` 文本嵌入（`embed_query` / `embed_documents`） |
| `17` | `OllamaEmbeddings` 本地嵌入模型 |

#### 子模块 B：提示词模板（18-21）

| 文件 | 学习要点 |
|------|---------|
| `18` | `PromptTemplate.from_template()` 模板化提示词 |
| `19` | `FewShotPromptTemplate`：示例模板 + 数据 + 前缀/后缀 |
| `20` | `format()` 返回字符串 vs `invoke()` 返回 `PromptValue` |
| `21` | `ChatPromptTemplate.from_messages()` + `MessagesPlaceholder` 动态插入历史消息 |

#### 子模块 C：Chain 链式调用（22-27）

| 文件 | 学习要点 |
|------|---------|
| `22` | 管道符 `|` 构建链：`prompt | model` |
| `23` | Python `__or__` 魔术方法实现原理（扩展理解） |
| `24` | `RunnableSequence` 类型：所有组件统一实现 `Runnable` 接口 |
| `25` | `StrOutputParser`：将 `AIMessage` 转为普通字符串 |
| `26` | `JsonOutputParser`：解析模型输出的 JSON，用于下游组件 |
| `27` | `RunnableLambda`：自定义转换函数，灵活处理中间结果 |

#### 子模块 D：会话记忆（28-29）

| 文件 | 学习要点 |
|------|---------|
| `28` | **临时记忆**：`InMemoryChatMessageHistory` + `RunnableWithMessageHistory` + session_id |
| `29` | **长期记忆**：自定义 `FileChatMessageHistory` 类，将对话历史持久化到本地文件 |

#### 子模块 E：文档加载器（30-33）

| 文件 | 学习要点 |
|------|---------|
| `30` | `CSVLoader`：加载 CSV 文件，支持指定分隔符、字段名 |
| `31` | `JSONLoader`：加载 JSON / JSONLines，基于 `jq_schema` 抽取字段 |
| `32` | `TextLoader` + `RecursiveCharacterTextSplitter`：文本加载与分割 |
| `33` | `PyPDFLoader`：PDF 加载，支持密码保护，支持 page/single 模式 |

#### 子模块 F：向量存储与 RAG（34-37）

| 文件 | 学习要点 |
|------|---------|
| `34` | `InMemoryVectorStore`：内存向量存储，增删查操作 |
| `35` | `Chroma`：持久化向量数据库，支持 `filter` 过滤检索 |
| `36` | **完整 RAG**：向量检索 → 构建带参考资料的提示词 → LLM 生成回答 |
| `37` | **RunnablePassthrough**：优雅构建 RAG 流水线，`retriever` + `format_func` 自动组合 |

---

## 🚀 学习路线建议

### 按阶段循序渐进

```
第一阶段：OpenAI 库基础
    ↓
第二阶段：提示词优化（Few-shot）
    ↓
第三阶段 A：LangChain 模型接入 → 嵌入模型
    ↓
第三阶段 B：提示词模板 → Chain 链
    ↓
第三阶段 C：输出解析器 → 会话记忆
    ↓
第三阶段 D：文档加载器 → 文本分割
    ↓
第三阶段 E：向量存储 → RAG 完整流水线（最终目标）
```

### 建议前置知识

- Python 基础（推荐预习 `data/Python基础语法.txt`，涵盖：变量、流程控制、函数、面向对象、装饰器、迭代器、正则表达式等）
- 对 LLM / 大模型的基本认知

---

## 💡 核心 RAG 流水线

最终在 `37RunnablePassThrough使用.py` 中实现的完整 RAG 流水线：

```python
chain = (
    {"input": RunnablePassthrough(), "context": retriever | format_func}
    | prompt
    | model
    | StrOutputParser()
)

result = chain.invoke("用户的提问")
```

**执行流程：**
1. `RunnablePassthrough()` 将用户输入透传
2. `retriever` 从向量库检索相关文档
3. `format_func` 格式化检索结果为参考文字
4. `prompt` 组装最终的提示词（参考 + 问题）
5. `model` 调用大模型生成回答
6. `StrOutputParser` 提取纯文本输出

---

## 📝 数据说明

`03LangChain_RAG开发/data/` 目录中的示例数据：

- **info.csv**：关于「黑马程序员」「传智教育」的信息语料（用于向量检索）
- **stu.csv**：学生信息（姓名/年龄/性别/爱好）
- **stu.json / stus.json**：JSON 格式学生数据
- **stu_json_lines.json**：JSONLines 格式数据
- **Python基础语法.txt**：Python 语法参考文档（用于文本分割实验）
- **pdf1.pdf / pdf2.pdf**：PDF 测试文件（pdf2 有密码保护 `itheima`）

---

## ⚙️ 常见问题

**Q：修改了代码中的 base_url 但仍无法连接？**
确保已安装对应依赖并设置正确的 API Key。阿里云百炼需在 [官网](https://bailian.console.aliyun.com/) 获取 API Key。

**Q：Ollama 连接失败？**
确认 Ollama 服务正在运行：`ollama list` 查看已拉取的模型列表。

**Q：`langchain_community` 导入报错？**
```bash
pip install --upgrade langchain langchain-community
```

**Q：Chroma 向量数据库报错？**
```bash
pip install chromadb langchain-chroma
```

---

## 📚 扩展参考

- [LangChain 官方文档](https://python.langchain.com/)
- [阿里云百炼大模型服务平台](https://bailian.console.aliyun.com/)
- [Ollama 本地模型运行](https://ollama.com/)
- [Chroma 向量数据库](https://www.trychroma.com/)

---

## 🎯 学习目标

完成本项目后，你将能够：

1. ✅ 使用 OpenAI 兼容 SDK 调用各类大模型
2. ✅ 设计高质量的 Few-shot 提示词完成分类、抽取、匹配任务
3. ✅ 使用 LangChain 框架快速构建 LLM 应用
4. ✅ 掌握提示词模板（PromptTemplate / ChatPromptTemplate / FewShotPromptTemplate）
5. ✅ 利用 Chain 链式组合多个处理步骤
6. ✅ 实现会话记忆（临时记忆 + 文件持久化）
7. ✅ 加载多种格式的文档数据（CSV / JSON / PDF / TXT）
8. ✅ 构建向量数据库并实现相似度检索
9. ✅ **搭建完整的 RAG（检索增强生成）智能体**
