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