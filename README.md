# AI-Powered RAG Application with MongoDB

An intelligent Retrieval-Augmented Generation (RAG) system built using **Python, MongoDB Vector Search, OpenAI GPT-5.5, and Voyage AI embeddings** for semantic document retrieval and context-aware question answering.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![MongoDB](https://img.shields.io/badge/MongoDB-Vector_Search-green)
![LLM](https://img.shields.io/badge/LLM-Integrated-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
---

## Overview

This project enables users to upload PDF documents, convert them into vector embeddings, store them in MongoDB Atlas, and query them using natural language.

The system retrieves semantically relevant document chunks and generates accurate AI-powered responses grounded in your own content.

---

## Features

- 📚 **Document Question Answering**  
  Ask questions from your PDF documents and receive context-aware responses.

- 🔍 **Semantic Search & Retrieval**  
  Retrieves relevant chunks using embedding similarity search.

- ⚡ **MongoDB Vector Search**  
  Fast and scalable vector-based retrieval using MongoDB Atlas.

- 🤖 **AI-Powered Responses**  
  Uses OpenAI GPT-5.5 to generate grounded answers from retrieved context.

- 🏷️ **Metadata Enrichment**  
  Automatically generates titles, keywords, and code indicators for chunks.

---

## Tech Stack

- Python 3.8+
- MongoDB Atlas
- MongoDB Vector Search
- OpenAI GPT-5.5
- Voyage AI Embeddings (`voyage-3-large`)

---

## Prerequisites

Before getting started, ensure you have:

- ✅ MongoDB Atlas Cluster
- ✅ MongoDB Connection String
- ✅ OpenAI API Key
- ✅ Voyage AI API Key
- ✅ Python 3.8+

---

## Project Setup

### 1. Clone Repository

```bash
git clone https://github.com/Siva-Dev-001/llm-rag-mongodb.git
cd llm-rag-mongodb
```

---

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux

```bash
python -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure API Keys

Create `.env`:

```python
LLM_API_KEY = "your_openai_api_key_here"
VOYAGE_API_KEY = "your_voyage_api_key_here"
MONGODB_URI = "your_mongodb_connection_string_here"
```

---

## API Key Setup

### MongoDB URI
Get from MongoDB Atlas:

**Cluster → Connect → Drivers**

---

### OpenAI API Key
Generate from:

https://platform.openai.com/api-keys

---

### Voyage AI API Key
Create free API key from:

https://www.voyageai.com/

---

## Usage

---

### Step 1: Load and Process Documents

Run:

```bash
python load_data.py
```

This process performs:

- 📄 PDF loading and cleaning
- ✂️ Text chunking  
  - Chunk size: 500
  - Overlap: 150
- 🏷️ Metadata generation
- 🧠 Embedding creation
- 💾 MongoDB insertion

> Note: Initial processing may take a few minutes.

---

### Step 2: Create MongoDB Vector Search Index

Navigate to:

**Atlas → Search & Vector Search**

Create index with:

- **Database:** `book_mongodb_chunks`
- **Collection:** `chunked_data`
- **Index Name:** `vector_index`

### Index Configuration

```json
{
  "fields": [
    {
      "numDimensions": 1024,
      "path": "embedding",
      "similarity": "dotProduct",
      "type": "vector"
    },
    {
      "path": "hasCode",
      "type": "filter"
    }
  ]
}
```

> Important: Wait until index status becomes **Ready**.

---

### Step 3: Run RAG Query System

```bash
python rag.py
```

---

### Step 4: Customize Queries

Update query inside `rag.py`:

```python
print(query_data("What is the difference between a collection and database in MongoDB?"))
```

Example queries:

```python
"What are the benefits of MongoDB Atlas?"
"How do I create an index in MongoDB?"
"Explain MongoDB aggregation pipeline"
```

---

## Example Output

### Query

```text
What is the difference between a collection and database in MongoDB?
```

### Response

```text
A database in MongoDB is a container that holds collections, while a collection is a grouping of documents. Think of a database as a filing cabinet and collections as folders containing related files.
```

---

## System Workflow

### 1. Document Processing
PDF documents are cleaned and chunked.

### 2. Embedding Generation
Chunks converted into vectors using Voyage AI.

### 3. Semantic Retrieval
Relevant chunks fetched using vector similarity.

### 4. Context Assembly
Top chunks merged into prompt context.

### 5. Answer Generation
GPT-4 generates grounded responses.

---

## Project Structure

```bash
llm-rag-mongodb/
│
├── sample_files/
├── load_data.py
├── rag.py
├── key_param.py
├── requirements.txt
└── README.md
```

---

## Troubleshooting

### No vector index found

Ensure vector search index exists and status is **Ready**.

---

### Authentication failed

Check:

- OpenAI API Key
- Voyage API Key
- MongoDB URI

---

### Module not found

Activate virtual environment:

```bash
source venv/bin/activate
```

or

```bash
venv\Scripts\activate
```

---

### File not found

Ensure PDF is inside:

```bash
sample_files/
```

---

## Future Improvements

- Chat history memory
- Web UI with Streamlit/React
- Multi-document querying
- Hybrid search (keyword + vector)
- Agentic workflows

---

## Learning Outcomes

Through this project:

- Learned RAG architecture design
- Implemented vector search workflows
- Worked with embeddings and semantic retrieval
- Improved LLM response grounding
- Explored MongoDB Atlas AI capabilities

---

## License

MIT License

---

## Author

**Siva R**

Python Developer | Django | AWS | MongoDB | GenAI | RAG Systems

GitHub: https://github.com/Siva-Dev-001
LinkedIn: https://linkedin.com/in/ramu-siva