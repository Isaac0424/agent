from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.tools import create_retriever_tool

from dotenv import load_dotenv
from pathlib import Path
load_dotenv()
DB_PATH = Path(__file__).resolve().parent / "database" / "chroma_db"
vectorstore=Chroma(
    persist_directory=DB_PATH,
    embedding_function=OpenAIEmbeddings(model="text-embedding-3-small"),
    collection_name="korean_pdf",
)

vectorstore.get()

retriever = vectorstore. as_retriever(search_kwargs={"k":3})

retriever_tool = create_retriever_tool(
    retriever,
    name="pdf_search",
    description="use this tool to search information from the Korean Spelling Rules PDF document",
)

if __name__=="__main__":
    response = retriever_tool.invoke("부엌 이 들어간 경우 어떻게 발음하나요?")
    print(response)
    print(DB_PATH)