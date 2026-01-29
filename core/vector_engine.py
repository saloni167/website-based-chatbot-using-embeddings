from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

VECTOR_PATH = "data/vectors"

def index_documents(text_blocks, meta):
    embedder = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    store = Chroma.from_texts(
        texts=text_blocks,
        metadatas=meta,
        embedding=embedder,
        persist_directory=VECTOR_PATH
    )
    store.persist()
    return store

def load_index():
    return Chroma(
        persist_directory=VECTOR_PATH,
        embedding_function=HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
    )
