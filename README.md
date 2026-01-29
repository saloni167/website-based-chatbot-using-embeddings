# website-based-chatbot-using-embeddings
🔍 Project Overview :
This project implements a website-grounded question answering chatbot that answers user queries strictly based on the content of a user-provided website. The system follows a Retrieval-Augmented Generation (RAG) approach with explicit control over crawling, chunking, embedding, retrieval, and response generation.

The focus of this implementation is clarity, originality, and system-level understanding, rather than relying on pre-built end-to-end chains.
The system uses LangChain’s retriever interface to perform similarity-based document retrieval using embeddings.

🤖 LLM Choice & Justification :
We use an LLM capable of instruction-following and grounded generation. The model is used strictly as a response generator with retrieved context, ensuring zero hallucination.

📦 Vector Database Choice :
ChromaDB was chosen because:-
1) Lightweight and fast
2) Easy local persistence
3) Perfect for prototype-to-production pipelines

   
