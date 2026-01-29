from langchain_text_splitters import RecursiveCharacterTextSplitter


def generate_chunks(text: str, size=550, overlap=70):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=size,
        chunk_overlap=overlap
    )
    return splitter.split_text(text)
