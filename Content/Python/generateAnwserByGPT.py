import openai

openai.api_key = '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'

def get_summary(keyword):
    # GPT-3.5에 요청할 대화 포맷 설정
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f" {keyword}에 대한 정보를 한국어로 제공."},
    ]

    # GPT-3.5에 대화 시작 요청
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        messages=conversation,
    )

    # GPT-3.5의 응답에서 정보 추출
    summary = response['choices'][0]['message']['content']
    return summary

# 사용자로부터 키워드 입력 받기
user_keyword = input("키워드를 입력하세요: ")

# 키워드에 대한 정보 요약 가져오기
result_summary = get_summary(user_keyword)

# 결과 출력 (한글로 설정했기 때문에 바로 출력 가능)
print(f" {result_summary}")

