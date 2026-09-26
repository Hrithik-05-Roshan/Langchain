# 🦜🔗 LangChain Learning Journey

> A structured, hands-on exploration of the LangChain ecosystem — from LLMs to Embeddings and beyond.

---

## 📊 Overall Progress

```
LangChain Models   ████████████████████░░░░░  ~75% Complete
Prompts            ░░░░░░░░░░░░░░░░░░░░░░░░░   Not Started
Chains             ░░░░░░░░░░░░░░░░░░░░░░░░░   Not Started
Memory             ░░░░░░░░░░░░░░░░░░░░░░░░░   Not Started
Agents             ░░░░░░░░░░░░░░░░░░░░░░░░░   Not Started
RAG / Retrieval    ░░░░░░░░░░░░░░░░░░░░░░░░░   Not Started
```

---

## 📁 Repository Structure

```
Langchain/
└── langchain_Models/
    ├── 1.LLMs/                      ✅ Complete
    │   └── 1_llmDemo.py
    ├── 2.ChatModels/                ✅ Complete
    │   ├── 1_chatmodel_openai.py
    │   ├── 2_chatmodel_anthropic.py
    │   ├── 3_chatmodel_gemini.py
    │   ├── 4_chatmodel_hf_api.py
    │   └── 5_chatmodel_hf_local.py
    ├── 3.EmbeddingModels/           ✅ Complete
    │   ├── 1_embeddingsmodel_openai_quesry.py
    │   ├── 2_embeddingsmodel_openai_docs.py
    │   ├── 3_embeddingsmodel_local.py
    │   └── 4_Project_documentSimillarity.py  🎯 Mini Project
    ├── requirements.txt
    └── test.py
```

---

## ✅ Completed: `langchain_Models/`

### 1️⃣ LLMs — Completion: `100%` ✅

> Old-style completion-based language models (non-chat interface).

| File | Model Used | Description |
|------|------------|-------------|
| `1_llmDemo.py` | `gpt-3.5-turbo-instruct` | Basic LLM invocation with OpenAI using `llm.invoke()` |

**Concepts Covered:**
- ✅ Loading environment variables with `python-dotenv`
- ✅ Initializing `OpenAI` LLM from `langchain_openai`
- ✅ Invoking an LLM with a text prompt

---

### 2️⃣ Chat Models — Completion: `100%` ✅

> Conversational models using the messages-based chat interface.

| File | Provider | Model Used | Description |
|------|----------|------------|-------------|
| `1_chatmodel_openai.py` | OpenAI | `gpt-4` | Chat invocation with temperature & token control |
| `2_chatmodel_anthropic.py` | Anthropic | `claude-3.5-sonnet` | Chat invocation using Claude |
| `3_chatmodel_gemini.py` | Google | `gemini-flash` | Chat invocation using Gemini, accessing response content |
| `4_chatmodel_hf_api.py` | HuggingFace (API) | `Llama-3.1-8B-Instruct` | Chat via HuggingFace Inference API Endpoint |
| `5_chatmodel_hf_local.py` | HuggingFace (Local) | `SmolLM2-135M-Instruct` | Chat running a model **locally** via `HuggingFacePipeline` |

**Concepts Covered:**
- ✅ `ChatOpenAI` with `temperature` & `max_completion_tokens` params
- ✅ `ChatAnthropic` — Claude integration
- ✅ `ChatGoogleGenerativeAI` — Gemini integration, structured response parsing
- ✅ `HuggingFaceEndpoint` + `ChatHuggingFace` — remote API inference
- ✅ `HuggingFacePipeline` + `ChatHuggingFace` — fully local inference

---

### 3️⃣ Embedding Models — Completion: `100%` ✅

> Converting text into dense vector representations for semantic search and similarity.

| File | Provider | Model Used | Description |
|------|----------|------------|-------------|
| `1_embeddingsmodel_openai_quesry.py` | OpenAI | `text-embeddings-3-large` | Embed a single query string |
| `2_embeddingsmodel_openai_docs.py` | OpenAI | `text-embeddings-3-large` | Embed multiple documents at once |
| `3_embeddingsmodel_local.py` | HuggingFace (Local) | `SmolLM2-135M-Instruct` | Run embeddings locally using `HuggingFaceEmbeddings` |
| `4_Project_documentSimillarity.py` | Google | `gemini-embedding-001` | 🎯 **Mini Project** — Document similarity search using cosine similarity |

**Concepts Covered:**
- ✅ `OpenAIEmbeddings` — `embed_query()` for single strings
- ✅ `OpenAIEmbeddings` — `embed_documents()` for batch documents
- ✅ `HuggingFaceEmbeddings` — local embedding without API key
- ✅ `GoogleGenerativeAIEmbeddings` — Gemini embedding model
- ✅ Cosine similarity with `sklearn.metrics.pairwise.cosine_similarity`
- ✅ Ranking documents by semantic similarity score

---

## 🎯 Mini Projects Completed

### 📄 Document Similarity Finder
> **File:** `langchain_Models/3.EmbeddingModels/4_Project_documentSimillarity.py`

**What it does:**
- Takes a list of cricket player descriptions as documents
- Takes a user query (e.g., *"Tell me about Jasprit Bumrah"*)
- Embeds both documents and query using **Google's Gemini Embedding model**
- Uses **cosine similarity** to find and return the most semantically relevant document
- Prints the match and its similarity score

**Tech Stack:** `LangChain` + `GoogleGenerativeAIEmbeddings` + `scikit-learn` + `numpy`

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- API keys for: OpenAI, Anthropic, Google Gemini, HuggingFace (as needed)

### Installation

```bash
# Clone the repository
git clone https://github.com/Hrithik-05-Roshan/Langchain.git
cd Langchain

# Install all dependencies
pip install -r langchain_Models/requirements.txt
```

### Environment Setup

Create a `.env` file in the `langchain_Models/` directory:

```env
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
GOOGLE_API_KEY=your_google_gemini_key_here
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
```

### Run Any Script

```bash
cd langchain_Models

# Test LangChain installation
python test.py

# Run any demo
python 1.LLMs/1_llmDemo.py
python 2.ChatModels/1_chatmodel_openai.py
python 3.EmbeddingModels/4_Project_documentSimillarity.py
```

---

## 🛠️ Tech Stack & Dependencies

| Package | Purpose |
|---------|---------|
| `langchain` | Core LangChain framework |
| `langchain-core` | Base abstractions and primitives |
| `langchain-openai` | OpenAI LLM & Chat models |
| `langchain-anthropic` | Anthropic Claude integration |
| `langchain-google-genai` | Google Gemini integration |
| `langchain-huggingface` | HuggingFace API & local models |
| `openai` | OpenAI Python client |
| `google-generativeai` | Google GenAI client |
| `transformers` | HuggingFace Transformers |
| `huggingface-hub` | HuggingFace Hub client |
| `python-dotenv` | Environment variable management |
| `scikit-learn` | Cosine similarity computation |
| `numpy` | Numerical operations |

---

## 🗺️ Learning Roadmap

- [x] **Module 1 — LLM Models** → Completion-based LLMs
- [x] **Module 2 — Chat Models** → Multi-provider conversational AI
- [x] **Module 3 — Embedding Models** → Semantic vector representations + similarity project
- [ ] **Module 4 — Prompt Templates** → PromptTemplate, ChatPromptTemplate, FewShot
- [ ] **Module 5 — Chains** → LLMChain, SequentialChain, LCEL
- [ ] **Module 6 — Memory** → ConversationBufferMemory, Summary Memory
- [ ] **Module 7 — Agents & Tools** → ReAct, Tool use, Custom Tools
- [ ] **Module 8 — RAG Pipeline** → Document loaders, Vector stores, Retrievers

---

## 👤 Author

**Hrithik Roshan**
- GitHub: [@Hrithik-05-Roshan](https://github.com/Hrithik-05-Roshan)

---

<p align="center">
  <i>Built while learning LangChain — one module at a time 🚀</i>
</p>
