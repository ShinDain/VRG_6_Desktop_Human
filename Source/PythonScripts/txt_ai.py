import openai

# OpenAI API 키 설정
OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY


def chat_with_gpt(prompt):
    # ChatGPT에 대화 요청을 보내기.
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )

    # 응답에서 생성된 텍스트를 가져오기.
    reply = response.choices[0].text.strip()

    return reply


# 사용자와 대화하기
print("ChatGPT: 안녕하세요! 무엇을 도와드릴까요?")
while True:
    user_input = input("사용자: ")
    if user_input.lower() == '종료':
        print("ChatGPT: 대화를 종료합니다. 감사합니다!")
        break

    # 사용자 입력을 기반으로 ChatGPT와 대화
    prompt = f"사용자: {user_input}\nChatGPT:"
    response = chat_with_gpt(prompt)

    # ChatGPT의 응답 출력
    print(response)

# ############################################################

import openai
import requests
from bs4 import BeautifulSoup

# OpenAI GPT-3.5 API 키 설정
openai.api_key = "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"

def get_text_from_url(url):
    # 주어진 URL에서 웹 페이지의 본문 텍스트를 추출
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join([paragraph.get_text() for paragraph in paragraphs])
        return text
    except Exception as e:
        print(f"Error fetching content from the URL: {e}")
        return None

def summarize_text(text):
    # OpenAI GPT-3.5를 사용하여 텍스트 요약
    try:
        response = openai.Completion.create(
            engine="text-davinci-003.5",
            prompt=text,
            max_tokens=150  # 요약된 텍스트의 최대 토큰 수
        )
        summary = response['choices'][0]['text'].strip()
        return summary
    except Exception as e:
        print(f"Error summarizing text: {e}")
        return None

if __name__ == "__main__":
    # 사용자로부터 텍스트 또는 URL을 입력 받음
    user_input = input("Enter the text or URL you want to summarize: ")

    # 입력이 URL인 경우 웹 페이지에서 본문 텍스트를 추출
    if user_input.startswith("http"):
        content = get_text_from_url(user_input)
    else:
        content = user_input

    if content:
        # 텍스트를 요약
        summary = summarize_text(content)

        if summary:
            # 요약 결과 출력
            print("\nSummary:")
            print(summary)
        else:
            print("Failed to generate summary.")
    else:
        print("No content to summarize.")
