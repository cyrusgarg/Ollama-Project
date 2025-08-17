#ingest pdf files

#send chunks to the embedded model 
#save the embeddings to a vector database
#PERFORM SIMILARITY SEARCH ON THE VECTOR DATABASE TO FIND RELEVANT CHUNKS
#RETRIEVE THE RELEVANT CHUNKS AND PRESENT THEM TO THE USER

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import OnlinePDFLoader

doc_path="./data/BOI.pdf"
model="llama3.2"

if doc_path:
    loader= PyPDFLoader(
        file_path=doc_path
        )
    data=loader.load()
    print(f"Loaded documents from {doc_path}")
else:
    print("upload a pdf file to continue")

content= data[0].page_content
#print(f"Content of the first page: {content[:500]}...")  # Print first 500 characters for brevity

#extract text from pdf files and split into chunks
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

#split and chunk the text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1200,  # Adjust chunk size as needed
    chunk_overlap=300  # Adjust overlap as needed
)
chunks = text_splitter.split_documents(data)
# print(f"Number of chunks created: {len(chunks)}")
# print(f"First chunk content: {chunks[0]}...")  # Print first 500 characters for brevity

#Add to vector database
import ollama
ollama.pull("nomic-embed-text")

vector_db= Chroma.from_documents(
    documents=chunks,
    embedding=OllamaEmbeddings(model="nomic-embed-text"),
    collection_name="simple-rag"  # Name your collection
)

print("Vector database created and populated with document chunks.")

#Retrieve relevant chunks based on user query
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain.retrievers.multi_query import MultiQueryRetriever

llm = ChatOllama(model=model)

QUERY_PROMPT= PromptTemplate(
    template="You are a helpful assistant. Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. \n\nQuestion: {question}\nHelpful Answer:",
    input_variables=[ "question"],
)

retriever= MultiQueryRetriever.from_llm(
    vector_db.as_retriever(),llm, prompt=QUERY_PROMPT
)


#RAG prompt
template="""Answer the question based on the context below.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
{context}
Question: {question}"""


prompt= ChatPromptTemplate.from_template(template)

chain=(
    {"context": retriever, "question": RunnablePassthrough()} 
    | prompt 
    | llm
    | StrOutputParser()
)

res= chain.invoke(input=("what is the document about?"))
# res= chain.input(input=("how to report BOI?"))
print(res)