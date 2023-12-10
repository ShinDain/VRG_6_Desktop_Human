import openai
import requests
from bs4 import BeautifulSoup
import text

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

def scrape_page_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text() for p in paragraphs])
        return content
    except Exception as e:
        print(f"Error scraping content from {url}: {e}")
        return None

def generate_summary(text):
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": text}
    ]

    response = generate_response(conversation)

    return response

def initialize_conversation():
    return [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "안녕하세요!"}
    ]

# 초기 대화 설정
conversation = initialize_conversation()

while True:
    user_input = input("User: ")

    if user_input.startswith("http"):
        page_content = text.get_text_from_url(user_input)
        # print(page_content)

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









