# website-based-chatbot-using-embeddings
🔍 Project Overview :
This project implements an AI-powered website chatbot that answers user questions strictly based on the content of a provided website. The system uses web crawling, text chunking, embeddings, and vector similarity search to ensure accurate and hallucination-free responses.


🤖 LLM Choice & Justification :
We use an LLM capable of instruction-following and grounded generation. The model is used strictly as a response generator with retrieved context, ensuring zero hallucination.

📦 Vector Database Choice :
ChromaDB was chosen because:-
1) Lightweight and fast
2) Easy local persistence
3) Perfect for prototype-to-production pipelines

   
