from pymongo import MongoClient
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_voyageai import VoyageAIEmbeddings
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_transformers.openai_functions import (
    create_metadata_tagger,
)
from langchain.tools import tool

import key_param

# Set the MongoDB URI, DB, Collection Names

client = MongoClient(key_param.MONGODB_URI)
dbName = "book_mongodb_chunks"
collectionName = "chunked_data"
collection = client[dbName][collectionName]

loader = PyPDFLoader(".\sample_files\mongodb.pdf")
pages = loader.load()
cleaned_pages = []

for page in pages:
    if len(page.page_content.split(" ")) > 20:
        cleaned_pages.append(page)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=150)

schema = {
    "properties": {
        "title": {"type": "string"},
        "keywords": {"type": "array", "items": {"type": "string"}},
        "hasCode": {"type": "boolean"},
    },
    "required": ["title", "keywords", "hasCode"],
}

@tool
def information_extraction(text: str):
    """Extract information from text."""
    return {"result": text}
# llm = ChatOpenAI(
#     openai_api_key=key_param.LLM_API_KEY, temperature=0, model="gpt-5"
# )
llm = ChatGoogleGenerativeAI(
    google_api_key=key_param.GEMINI_API_KEY,
    model="gemini-3.5-flash",
    temperature=0,
)
llm_with_tools = llm.bind_tools([information_extraction])

document_transformer = create_metadata_tagger(metadata_schema=schema, llm=llm)

docs = document_transformer.transform_documents(cleaned_pages)

split_docs = text_splitter.split_documents(docs)

embeddings = VoyageAIEmbeddings(voyage_api_key=key_param.VOYAGE_API_KEY, model="voyage-3-large")


vectorStore = MongoDBAtlasVectorSearch.from_documents(
    split_docs, embeddings, collection=collection
)