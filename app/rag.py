from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


def load_pdf():
    pdf_path = "data/POM_Activity 2 (Piyush Kotkar).pdf"

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    print(f"Loaded {len(documents)} pages")

    return documents


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    return chunks


def create_embeddings():
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Embedding model loaded successfully")

    return embedding

def create_vector_store(chunks, embedding):
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory="chroma_db"
    )

    print("Vector Store Created Successfully!")

    return vector_store


def retrieve_documents(vector_store, query):
    results = vector_store.similarity_search(
        query,
        k=3
    )

    print(f"Retrieved {len(results)} relevant chunks")

    return results

def build_context(results):
    context = ""

    for doc in results:
        context += doc.page_content + "\n\n"

    return context