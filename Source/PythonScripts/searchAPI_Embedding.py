import os
import configparser

from langchain.utilities import GoogleSearchAPIWrapper
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

api_config = configparser.ConfigParser()
api_config.read_file(open('apidata.ini'))
os.environ['OPENAI_API_KEY'] = api_config["OPENAI"]["OTHER_KEY"]
os.environ['GOOGLE_CSE_ID'] = api_config["GOOGLE"]["CSE_ID"]
os.environ['GOOGLE_API_KEY'] = api_config["GOOGLE"]["API_KEY"]

def embeddings(query,dbDir):
    llm = OpenAI(temperature=0)

    make_searchWord_prompt = PromptTemplate(
        input_variables=["contents"],
        template="다음 문장에 대한 정보를 구글에 검색하기 위한 문장을 만들어 줘. '{contents}'"
    )

    searchSentence = llm(make_searchWord_prompt.format(contents=query))

    search = GoogleSearchAPIWrapper()
    result = search.run(searchSentence)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_text(result)
    
    if(os.path.isdir(dbDir) == False):
        os.mkdir(dbDir)

    embedding = OpenAIEmbeddings(model="text-embedding-ada-002", chunk_size=1 )
    
    vectordb = Chroma.from_texts(
        texts=texts, 
        embedding=embedding,
        persist_directory=dbDir)

    vectordb.persist()
    vectordb = None


def searchOpenAI(query,dbDir):
    embedding = OpenAIEmbeddings(model="text-embedding-ada-002",  chunk_size=1 )
    vectordb = Chroma( persist_directory=dbDir,  embedding_function=embedding)
    retriever = vectordb.as_retriever()

    ask_prompt = PromptTemplate(
        input_variables=["contents"],
        template="다음 질문을 한국어로 답해줘. 만약 최근에 대한 질문이라면 분명 너의 데이터에 있을테니 그 정보를 찾아서 답해줘.'{contents}'"
    )
    
    llm = ChatOpenAI(temperature=0)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff',retriever=retriever)
    llm_response = qa_chain(ask_prompt.format(contents=query))
    
    return llm_response["result"]

def chat_respons(query):
    #dbDir = os.getcwd() + '/VectorDB'
    dbDir = os.path.dirname(os.path.abspath(__file__)) + '/VectorDB'
    embeddings(query, dbDir)
    result = searchOpenAI(query, dbDir)
    return result

if __name__ == '__main__':
    print("Embedding을 이용한 인터넷 검색 AI 입니다.")
    query = input("질문사항을 입력해주세요: ")
    result = chat_respons(query)
    print(result)
    input("Press Enter to end Program")
