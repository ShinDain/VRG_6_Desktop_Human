import os
import configparser

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.agents import load_tools
from langchain.agents import initialize_agent

api_config = configparser.ConfigParser()
api_config.read_file(open('apidata.ini'))
os.environ['OPENAI_API_KEY'] = api_config["OPENAI"]["OTHER_KEY"]
os.environ['GOOGLE_CSE_ID'] = api_config["GOOGLE"]["CSE_ID"]
os.environ['GOOGLE_API_KEY'] = api_config["GOOGLE"]["API_KEY"]
os.environ['SERPER_API_KEY']= api_config["OPENAI"]["SERPER_KEY"]

ask_prompt = PromptTemplate(
    input_variables=["contents"],
    template="다음 질문을 150자 이내의 한국어로 답해줘. '{contents}'"
)

llm = OpenAI(temperature=0)

serper_chain = load_tools(["google-serper", "llm-math"], llm=llm)
serper_decider = initialize_agent(serper_chain,
                                  llm,
                                  agent="zero-shot-react-description",
                                  verbose=True)

def chat_respons(input_text):
    result = serper_decider.run(ask_prompt.format(contents=input_text))
    return result


if __name__ == '__main__':
    print("GoogleSerperAPI를 이용한 인터넷 검색 AI 입니다.")
    qurey = input("질문을 입력해주세요 : ")
    result = chat_respons(qurey)
    print(result)
    input("Press Enter to end Program")