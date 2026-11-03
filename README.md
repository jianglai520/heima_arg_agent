# 🤖 Heima RAG Agent — 黑马 RAG 智能体开发实战教程

> 一个循序渐进的大模型 RAG（检索增强生成）智能体开发学习项目，基于 Python + OpenAI 兼容接口 + LangChain 框架构建。
>
> 项目来源：**黑马程序员** 大模型开发课程配套代码

---

## 📋 项目概述

本项目是**从零入门大模型应用开发**的完整实战教程，分为三个逐步递进的学习阶段：

| 阶段 | 模块 | 内容 | 文件数 |
|------|------|------|--------|
| 1️⃣ | OpenAI 库的基础使用 | 调用大模型 API 的基础能力 | 5 |
| 2️⃣ | 提示词优化 | Prompt Engineering 实战 | 4 |
| 3️⃣ | LangChain RAG 开发 | 完整 RAG 流水线构建 | 29 |

涵盖的技术栈包括：**OpenAI SDK、DeepSeek / 阿里云百炼（通义千问）、Ollama 本地模型、LangChain 1.x、Chroma 向量数据库、文本嵌入、提示词模板、文档加载器、会话记忆** 等。

---

## 📂 项目结构

```
E:/heima_rag_agent/
├── 01OpenAI库的基础使用/            # 第一阶段：OpenAI SDK 入门
│   ├── 01测试api_key使用.py          # 测试 API Key 连通性（.env 读取配置）
│   ├── 02OpenAI库的基本使用.py       # OpenAI SDK 基本调用（system/assistant/user）
│   ├── 03OpenAI库的流式输出.py       # Streaming 流式输出
│   ├── 04OpenAI库带历史消息调用模型.py # 多轮对话历史消息传递
│   └── 05-代码调用Ollama的本地模型.py # 用 OpenAI SDK 访问 Ollama 本地模型
│
├── 02提示词优化/                    # 第二阶段：提示词工程
│   ├── 06提示词优化案例——金融文本分类.py   # Few-shot 金融文本分类
│   ├── 07json的基础使用.py                 # JSON 序列化/反序列化
│   ├── 08提示词优化案例——金融信息抽取.py    # Few-shot 金融信息抽取（输出 JSON）
│   └── 09提示词优化——金融文本匹配判断.py    # 文本语义匹配判断
│
├── 03LangChain_RAG开发/             # 第三阶段：LangChain + RAG 完整开发
│   ├── 10余弦相似度.py                      # 向量余弦相似度手动实现
│   ├── 11LangChain访问Qwen大模型.py         # Tongyi + 通义千问
│   ├── 12LangChain访问Ollama本地模型.py     # OllamaLLM + 本地模型
│   ├── 13LangChain流式输出.py               # LangChain 流式输出
│   ├── 14LangChain调用聊天模型.py           # ChatOpenAI（聊天模型）
│   ├── 15LangChain调用本地ollama聊天模型.py # ChatOllama 聊天模型
│   ├── 16LangChain消息的简写形式.py         # 消息元组简写 (role, content)
│   ├── 17LangChain文本嵌入模型使用.py       # DashScopeEmbeddings 文本嵌入
│   ├── 18LangChain文本嵌入模型使用(ollama).py # Ollama 本地嵌入模型
│   ├── 19通用提示词模板.py                  # PromptTemplate 基础
│   ├── 20FewShot提示词模板.py               # FewShotPromptTemplate
│   ├── 21模板类的format 和 invoke方法.py    # format() vs invoke()
│   ├── 22ChatPromptTemplate的使用.py        # 聊天提示词模板 + MessagesPlaceholder
│   ├── 23langchain中chain链的学习.py        # 链式调用（`|` 管道符）
│   ├── 24[扩展]python的或运算符的重写.py    # Python `__or__` 魔术方法原理
│   ├── 25Runnable接口源码查看.py            # Runnable 接口与 RunnableSequence
│   ├── 26StrOutputParser解析器.py           # 字符串输出解析器
│   ├── 27JsonOutputParser解析器.py          # JSON 输出解析器
│   ├── 28RunnableLambda解析器.py            # 自定义 Lambda 解析器
│   ├── 29临时会话记忆.py                    # InMemoryChatMessageHistory 临时记忆
│   ├── 30长期会话记忆.py                    # 自定义 FileChatMessageHistory 文件持久化
│   ├── 31CSVLoader.py                       # CSV 文档加载器
│   ├── 32JSONLoader.py                      # JSON/JSONLines 文档加载器
│   ├── 33TextLoader.py                      # 文本加载器 + RecursiveCharacterTextSplitter
│   ├── 34PDFLoader.py                       # PyPDFLoader PDF 加载器
│   ├── 35内存向量存储.py                    # InMemoryVectorStore 向量检索
│   ├── 36外部向量持久化存储.py              # Chroma 持久化向量数据库
│   ├── 37向量检索构建提示词.py              # 向量检索 + RAG 提示词构建
│   ├── 38RunnablePassThrough使用.py         # RunnablePassthrough 完整 RAG 流水线
│   ├── JSON格式在python中的转换             # JSON ↔ Python 对象转换笔记
│   ├── 管道符理解                           # Python `|` 管道符执行流程笔记
│   ├── data/                                # 示例数据文件
│   │   ├── info.csv                         # 黑马/传智信息语料（用于向量检索）
│   │   ├── stu.csv                          # 学生 CSV 数据
│   │   ├── stu.json                         # 单个 JSON 对象数据
│   │   ├── stus.json                        # JSON 数组数据
│   │   ├── stu_json_lines.json              # JSONLines 数据
│   │   ├── Python基础语法.txt               # Python 语法参考文档
│   │   ├── pdf1.pdf                         # PDF 文件 1
│   │   ├── pdf2.pdf                         # PDF 文件 2（密码保护）
│   │   └── pdf2密码                         # pdf2.pdf 的密码：itheima
│   ├── chroma_db/                           # Chroma 持久化目录（运行时生成，已忽略）
│   └── chat_history/                        # 会话记忆存储（运行时生成，已忽略）
│
├── .env                                    # 密钥配置（本地私有，已忽略）
├── .venv/                                  # Python 虚拟环境（已忽略）
└── README.md                               # 本文件
```

---

## 🔧 环境要求

### 1. Python 版本
- Python 3.10+（当前虚拟环境为 3.14.3）

### 2. 依赖安装

```bash
# 核心依赖
pip install openai python-dotenv
pip install langchain langchain-core langchain-community langchain-openai
pip install langchain-ollama langchain-text-splitters
pip install langchain-chroma chromadb numpy pypdf jq openpyxl
```

> 代码中实际出现的导入：`openai`、`dotenv`、`numpy`、`json`、`openpyxl`、
> `langchain_core`、`langchain_community`、`langchain_ollama`、`langchain_openai`、
> `langchain_text_splitters`、`langchain_chroma`。

### 3. 密钥配置（.env）

项目通过 `load_dotenv()` 从根目录 `.env` 读取配置，需要以下变量：

```dotenv
# DeepSeek / 阿里云百炼 OpenAI 兼容接口
DEEPSEEK_API_KEY=sk-xxx
DEEPSEEK_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1

# 百炼原生 SDK（DashScopeEmbeddings / Tongyi）
DASHSCOPE_API_KEY=sk-xxx
```

> `.env` 含真实密钥，**已在 `.gitignore` 中忽略，不要提交**。
> 各文件均保留了可替换的注释写法，也可直接把 key 写进代码（仅本地练习）。

### 4. 模型服务

项目混用两种模型来源，按文件注释切换即可：

#### 方式一：DeepSeek / 阿里云百炼（云端）

```python
client = OpenAI(
    base_url=os.getenv("DEEPSEEK_BASE_URL"),
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)
# 当前使用 model = "deepseek-flash"
# 备选：qwen3.7-max / qwen3.8-flash / qwen-max
```

#### 方式二：Ollama 本地模型

安装 [Ollama](https://ollama.com/) 后拉取模型：

```bash
ollama pull deepseek-r1:1.5b      # 对话模型
ollama pull qwen3-embedding:0.6b  # 嵌入模型
```

```python
client = OpenAI(base_url="http://localhost:11434/v1")
```

---

## 📖 模块详解

### 阶段 1：OpenAI 库的基础使用

学习通过 OpenAI 兼容 SDK 调用大模型 API 的基本操作。

| 文件 | 学习要点 |
|------|---------|
| `01` | `load_dotenv(override=True)` 读取配置；测试 API Key 连通性；流式解析 `reasoning_content` 与 `content` |
| `02` | 完整调用流程：创建 Client → 构建 messages → 调用模型 → 处理响应；角色体系（system/assistant/user） |
| `03` | `stream=True` 流式输出，`flush=True` 逐块打印 |
| `04` | 多轮对话历史维护，把 assistant 回复拼回 messages 让模型基于上下文回答 |
| `05` | 同一套 OpenAI SDK 直接指向 `http://localhost:11434/v1` 调用 Ollama 本地模型，对比云端与本地差异 |

**关键概念：**
- `messages` 列表结构：`system`（系统指令）、`assistant`（助手回复）、`user`（用户输入）
- 流式输出与普通输出的区别与适用场景

---

### 阶段 2：提示词优化

学习 Few-shot Prompt Engineering 技巧，应用于金融领域的文本任务。

| 文件 | 学习要点 |
|------|---------|
| `06` | **金融文本分类**：Few-shot 示例引导模型分类为「新闻报道/财务报道/公司公告/分析师报告」 |
| `07` | **JSON 基础**：`json.dumps/loads`、`ensure_ascii`、`indent` 等序列化细节（为结构化输出做准备） |
| `08` | **金融信息抽取**：按 `schema = ['日期','股票名称','开盘价','收盘价','成交量']` 抽取，输出 JSON |
| `09` | **文本匹配判断**：判断两段金融文本是否语义匹配（「是/不是」二分类） |

**关键概念：**
- **Few-shot Learning**：在 prompt 中提供输入-输出示例，引导模型理解任务
- **结构化输出**：要求模型以 JSON 格式返回结果，便于程序解析
- **金融场景**：文本分类、信息抽取、语义匹配三个典型 NLP 任务

---

### 阶段 3：LangChain RAG 开发

使用 LangChain 框架构建完整 RAG 流水线，是本项目的核心模块。

#### 子模块 A：模型接入（10-18）

| 文件 | 学习要点 |
|------|---------|
| `10` | 余弦相似度手动实现（点积 / 模长 → 向量检索的数学基础） |
| `11` | `langchain_community.llms.tongyi.Tongyi` 调用通义千问 `qwen-max` |
| `12` | `langchain_ollama.OllamaLLM` 调用本地 `deepseek-r1:1.5b` |
| `13` | LangChain 流式输出（`model.stream()`） |
| `14` | 聊天模型 `ChatOpenAI` + `HumanMessage/SystemMessage/AIMessage` |
| `15` | Ollama 聊天模型 `ChatOllama` |
| `16` | 消息简写：`("human", "内容")` 元组形式代替消息类对象 |
| `17` | `DashScopeEmbeddings` 文本嵌入（默认 `text-embedding-v1`，`embed_query` / `embed_documents`） |
| `18` | `OllamaEmbeddings` 本地嵌入模型 `qwen3-embedding:0.6b` |

#### 子模块 B：提示词模板（19-22）

| 文件 | 学习要点 |
|------|---------|
| `19` | `PromptTemplate.from_template()` 模板化提示词 |
| `20` | `FewShotPromptTemplate`：示例模板 + 数据 + 前缀/后缀 |
| `21` | `format()` 返回字符串 vs `invoke()` 返回 `PromptValue`；三者继承关系 |
| `22` | `ChatPromptTemplate.from_messages()` + `MessagesPlaceholder` 动态插入历史消息 |

#### 子模块 C：Chain 链式调用（23-28）

| 文件 | 学习要点 |
|------|---------|
| `23` | 管道符 `|` 构建链：`prompt | model`，上游输出即下游输入 |
| `24` | Python `__or__` 魔术方法实现原理（扩展理解） |
| `25` | `RunnableSequence` 类型：所有组件统一实现 `Runnable` 接口 |
| `26` | `StrOutputParser`：将 `AIMessage` 转为普通字符串 |
| `27` | `JsonOutputParser`：解析模型输出的 JSON，用于下游组件 |
| `28` | `RunnableLambda`：自定义转换函数，灵活处理中间结果 |

#### 子模块 D：会话记忆（29-30）

| 文件 | 学习要点 |
|------|---------|
| `29` | **临时记忆**：`InMemoryChatMessageHistory` + `RunnableWithMessageHistory` + session_id |
| `30` | **长期记忆**：自定义 `FileChatMessageHistory(BaseChatMessageHistory)`，用 `message_to_dict` / `messages_from_dict` 把历史存到 `chat_history/` |

#### 子模块 E：文档加载器（31-34）

| 文件 | 学习要点 |
|------|---------|
| `31` | `CSVLoader`：加载 CSV，支持 `delimiter`、`quotechar`、`source_column` |
| `32` | `JSONLoader`：加载 JSON / JSONLines，基于 `jq_schema` 抽取字段 |
| `33` | `TextLoader` + `RecursiveCharacterTextSplitter`：文本加载与分割 |
| `34` | `PyPDFLoader`：PDF 加载，支持密码（`itheima`）与 `page` / `single` 模式 |

#### 子模块 F：向量存储与 RAG（35-38）

| 文件 | 学习要点 |
|------|---------|
| `35` | `InMemoryVectorStore`：内存向量存储，`add_documents` / `similarity_search` |
| `36` | `Chroma`：持久化向量数据库，`persist_directory` + `filter` 过滤检索 |
| `37` | **完整 RAG**：向量检索 → 构建带参考资料的提示词 → LLM 生成回答 |
| `38` | **RunnablePassthrough**：`{"input": ..., "context": retriever | format_func}` 优雅编排 RAG 流水线 |

---

## 🚀 学习路线建议

### 按阶段循序渐进

```
第一阶段：OpenAI 库基础（01-05）
    ↓
第二阶段：提示词优化（06-09）
    ↓
第三阶段 A：LangChain 模型接入 → 嵌入模型（10-18）
    ↓
第三阶段 B：提示词模板 → Chain 链（19-28）
    ↓
第三阶段 C：会话记忆（29-30）
    ↓
第三阶段 D：文档加载器 → 文本分割（31-34）
    ↓
第三阶段 E：向量存储 → RAG 完整流水线（35-38，最终目标）
```

### 建议前置知识

- Python 基础（推荐预习 `data/Python基础语法.txt`，涵盖：变量、流程控制、函数、面向对象、装饰器、迭代器、正则表达式等）
- 对 LLM / 大模型的基本认知

---

## 💡 核心 RAG 流水线

`38RunnablePassThrough使用.py` 中实现的完整 RAG 流水线：

```python
chain = (
    {"input": RunnablePassthrough(), "context": retriever | format_func}
    | prompt
    | model
    | StrOutputParser()
)

result = chain.invoke(input_text)
```

**执行流程：**
1. `RunnablePassthrough()` 将用户输入原样透传为 `input`
2. `retriever`（`vector_store.as_retriever(search_kwargs={"k": 2})`）检索相关文档 → `list[Document]`
3. `format_func` 把检索结果拼成参考文字
4. `prompt` 组装最终提示词（参考资料 + 用户提问）
5. `model` 调用大模型生成回答
6. `StrOutputParser` 提取纯文本输出

> 各组件输入/输出契约：`retriever` 收 `str`、出 `list[Document]`；`prompt` 收 `dict`、出 `PromptValue`。

---

## 📝 数据说明

`03LangChain_RAG开发/data/` 目录中的示例数据：

- **info.csv**：关于「黑马程序员」「传智教育」的信息语料（用于向量检索）
- **stu.csv**：学生信息（姓名/年龄/性别/爱好）
- **stu.json / stus.json**：单个对象 / 数组两种 JSON 格式学生数据
- **stu_json_lines.json**：JSONLines 格式数据
- **Python基础语法.txt**：Python 语法参考文档（用于文本分割实验）
- **pdf1.pdf / pdf2.pdf**：PDF 测试文件（pdf2 有密码保护）
- **pdf2密码**：记录了 pdf2.pdf 的密码 `itheima`

**运行时产物（不纳入版本管理）：**
- `chroma_db/`：Chroma 持久化数据
- `chat_history/`：长期会话记忆文件

---

## ⚙️ 常见问题

**Q：修改了代码中的 base_url 但仍无法连接？**
确保 `.env` 中的 `DEEPSEEK_API_KEY` / `DEEPSEEK_BASE_URL` 与代码一致，并注意 `load_dotenv(override=True)` 会覆盖系统环境变量。

**Q：Ollama 连接失败？**
确认 Ollama 服务正在运行：`ollama list` 查看已拉取的模型列表；本地默认地址为 `http://localhost:11434/v1`。

**Q：`langchain_community` 导入报错？**
```bash
pip install --upgrade langchain langchain-community
```

**Q：Chroma 向量数据库报错？**
```bash
pip install chromadb langchain-chroma
```

**Q：`Tongyi`/`DashScopeEmbeddings` 提示额度不足？**
云端 `qwen-max` 免费额度可能已耗尽，可切到 Ollama 本地模型（文件内均有注释写法）。

---

## 📚 扩展参考

- [LangChain 官方文档](https://python.langchain.com/)
- [阿里云百炼大模型服务平台](https://bailian.console.aliyun.com/)
- [Ollama 本地模型运行](https://ollama.com/)
- [Chroma 向量数据库](https://www.trychroma.com/)

---

## 🎯 学习目标

完成本项目后，你将能够：

1. ✅ 使用 OpenAI 兼容 SDK 调用各类大模型（云端 / Ollama 本地）
2. ✅ 设计高质量的 Few-shot 提示词完成分类、抽取、匹配任务
3. ✅ 使用 LangChain 框架快速构建 LLM 应用
4. ✅ 掌握提示词模板（PromptTemplate / ChatPromptTemplate / FewShotPromptTemplate）
5. ✅ 利用 Chain 链式组合多个处理步骤
6. ✅ 实现会话记忆（临时记忆 + 文件持久化）
7. ✅ 加载多种格式的文档数据（CSV / JSON / PDF / TXT）
8. ✅ 构建向量数据库并实现相似度检索
9. ✅ **搭建完整的 RAG（检索增强生成）智能体**
