import openai
import requests
from bs4 import BeautifulSoup

openai.api_key = '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'

def generate_response(conversation):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        messages=conversation,
        temperature=0.2,
        max_tokens=1000,
        frequency_penalty=0.0
    )
    return response['choices'][0]['message']['content'].strip()

def get_text_from_url(url):
    # 웹페이지 내용 가져오기
    response = requests.get(url)
    if response.status_code == 200:
        # BeautifulSoup을 사용하여 HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # 링크에 "sports.news.naver.com"이 포함되어 있는지 확인
        if "sports.news.naver.com" in url:
            # sports.news.naver.com인 경우 다른 방식으로 내용 추출
            # 예: 기사 내용을 포함하는 <div> 태그 추출
            article_tag = soup.find('div', class_='content')

            # <div> 태그가 존재하면 해당 내용을 추출, 없으면 빈 문자열 반환
            if article_tag:
                sports_content = article_tag.get_text(separator=' ', strip=True)
                return sports_content
            else:
                print("스포츠 기사 내용을 찾을 수 없습니다.")
                return ""

        elif "news.naver.com" in url:
            # news.naver.com인 경우 다른 방식으로 내용 추출
            # 기사 내용을 포함하는 <article> 태그 추출
            article_tag = soup.find('article', class_='go_trans _article_content')

            # <article> 태그가 존재하면 해당 내용을 추출, 없으면 빈 문자열 반환
            if article_tag:
                news_content = article_tag.get_text(separator=' ', strip=True)
                return news_content
            else:
                print("기사 내용을 찾을 수 없습니다.")
                return ""
        else:
            # 다른 경우 기존 방식으로 본문 내용 추출
            body_content = soup.find('body').get_text(separator=' ', strip=True)
            return body_content
    else:
        print(f"에러: {response.status_code}")
        return None

def generate_summary(text):
    conversation = [
        {"role": "system", "content": "도움이 필요한 어시스턴트입니다."},
        {"role": "user", "content": text}
    ]

    response = generate_response(conversation)

    return response

def initialize_conversation():
    return [
        {"role": "system", "content": "도움이 필요한 어시스턴트입니다."},
        {"role": "user", "content": "안녕하세요!"}
    ]

def chat():
    # 초기 대화 설정
    conversation = initialize_conversation()

    while True:
        user_input = input("사용자: ")

        if user_input.startswith("http"):
            page_content = get_text_from_url(user_input)

            if page_content:
                summary = generate_summary(f'지금 뒤에 오는 본문 요약해줘, {page_content}')
                print("ChatGPT:", summary)
                conversation.extend([{"role": "user", "content": user_input}, {"role": "assistant", "content": summary}])
            else:
                print("ChatGPT: 페이지 본문을 가져올 수 없습니다.")
        else:
            conversation.append({"role": "user", "content": user_input})
            response = generate_summary(user_input)
            print("ChatGPT:", response)
            conversation.extend([{"role": "assistant", "content": response}])

        # 대화 기록을 일정한 크기(예: 5개 메시지)로 유지
        conversation = conversation[-5:]

chat()
