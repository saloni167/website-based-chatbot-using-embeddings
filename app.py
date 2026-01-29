import streamlit as st
from core.web_reader import read_website
from core.chunker import generate_chunks
from core.vector_engine import index_documents, load_index
from core.responder import answer_question


# st.title("🚀 App Loaded Successfully")
# st.write("If you see this, Streamlit is working.")


st.set_page_config(page_title="Website QA Bot")
st.title("🌐 Website Question Answering Bot")

url = st.text_input("Enter website URL")

if st.button("Process Website"):
    data = read_website(url)

    if not data:
        st.error("Could not read website.")
    else:
        chunks = generate_chunks(data["content"])
        metadata = [{"source": data["source"], "title": data["title"]} for _ in chunks]
        index_documents(chunks, metadata)
        st.success("Website indexed successfully!")

question = st.text_input("Ask your question")

if question:
    db = load_index()
    reply = answer_question(question, db)
    st.write(reply)
