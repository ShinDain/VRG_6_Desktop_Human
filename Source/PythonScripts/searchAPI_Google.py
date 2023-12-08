import os
import configparser

from langchain.agents import Tool
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.agents import initialize_agent
from langchain.prompts import PromptTemplate

api_config = configparser.ConfigParser()
api_config.read_file(open('apidata.ini'))
os.environ['OPENAI_API_KEY'] = api_config["OPENAI"]["OTHER_KEY"]
os.environ['GOOGLE_CSE_ID'] = api_config["GOOGLE"]["CSE_ID"]
os.environ['GOOGLE_API_KEY'] = api_config["GOOGLE"]["API_KEY"]

search = GoogleSearchAPIWrapper()
tools = [
    Tool(
    name ="Search" ,
    func=search.run,
    description="useful when you need to answer questions about current events"
    ),
]
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
llm=ChatOpenAI(temperature=0)
agent_chain = initialize_agent(tools, llm, agent="chat-conversational-react-description", verbose=True, memory=memory)

ask_prompt = PromptTemplate(
    input_variables=["contents"],
    template="다음 질문을 한국어로 답해줘. '{contents}'"
)

def chat_respons(input_text):
    response = agent_chain.run(ask_prompt.format(contents=input_text))
    return response

if __name__ == '__main__':
    print("GoogleSearchAPI를 이용한 인터넷 검색 AI 입니다.")
    query = input("질문사항을 입력해주세요: ")
    result = chat_respons(query)
    print(result)
    input("Press Enter to end Program")