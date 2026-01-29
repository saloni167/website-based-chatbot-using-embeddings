# website-based-chatbot-using-embeddings

1️⃣ Project Overview:

This project implements an AI-powered website-based chatbot that answers user questions strictly based on the content of a user-provided website. The system follows a Retrieval-Augmented Generation (RAG) approach, where website content is crawled, processed into embeddings, stored in a vector database, and queried to generate accurate, context-aware answers.

The chatbot is designed to avoid hallucinations and respond with a fixed message when the requested information is not present on the website.

2️⃣ Architecture Explanation:

High-Level Architecture:

User enters Website URL
        ↓
Website Crawling & Text Extraction
        ↓
Text Cleaning & Chunking
        ↓
Embedding Generation
        ↓
Persistent Vector Database
        ↓
User Question
        ↓
Similarity-Based Retrieval
        ↓
LLM Response (Context-Only)

Architectural Principles:
- Explicit control over each stage (crawl → chunk → embed → retrieve → generate)
- No black-box QA chains
- Strict grounding of answers in retrieved website content
- Persistent embeddings to avoid recomputation

3️⃣ Frameworks Used:
LangChain:

LangChain is used for:
- Text chunking (RecursiveCharacterTextSplitter)
- Embedding and vector database abstractions
- Retriever interfaces
- Pre-built QA chains (e.g., RetrievalQA) are intentionally avoided to maintain transparency and originality.

LangGraph (Optional / Advanced Version):

In the advanced version of this project, LangGraph is used to:
- Explicitly model retrieval and generation as graph nodes
- Maintain session-level conversational state
- Improve debuggability and production readiness

4️⃣ LLM Model Used and Justification:
* Model Used : OpenAI-compatible Chat Model (e.g., GPT-based)

* Why This Model?
- Strong instruction-following capability
- Reliable performance for grounded question answering
- Deterministic behavior when used with temperature = 0
- Well-suited for context-constrained generation

The LLM is used only as a response generator, never as a knowledge source.

5️⃣ Vector Database Used and Justification:
* Vector Database : ChromaDB

* Why ChromaDB?
- Lightweight and easy to set up
- Supports local persistence
- Efficient similarity search for embeddings
- Ideal for prototype-to-production workflows

Embeddings are stored on disk and reused across queries, as required by the assignment.

6️⃣ Embedding Strategy:
1) Embedding Model: sentence-transformers/all-MiniLM-L6-v2
2) Chunk Size: ~500–600 characters
3) Chunk Overlap: ~70–80 characters
4) Metadata Stored:

* Source URL
* Page title (if available)
* This strategy balances:

- Semantic coherence
- Retrieval accuracy
- Computational efficiency

7️⃣ Setup and Run Instructions:
Prerequisites:
* Python 3.9+
* pip installed

Installation:
pip install -r requirements.txt

Running the Application:
streamlit run app.py

Usage Flow:
1) Enter a valid website URL
2) Click Process Website to index content
3) Ask questions related to the website
4) Receive grounded answers or a fixed fallback response

8️⃣ Assumptions, Limitations, and Future Improvements:
Assumptions:
1) The website contains readable HTML content
2) One website is indexed per session
3) Users ask questions relevant to the indexed website

Limitations:
1) JavaScript-heavy websites may not fully render
2) No multi-website indexing in a single session
3) No authentication or rate limiting
4) Limited to short-term, session-scoped memory

Future Improvements:
1) Multi-page and deep crawling
2) Document reranking for improved retrieval quality
3) Answer confidence scoring
4) Streaming LLM responses
5) Cloud deployment (Docker / Kubernetes)
6) Multi-user session management


   
