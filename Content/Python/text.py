import requests
from bs4 import BeautifulSoup


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


if __name__ == "__main__":
    # 사용자로부터 링크 입력 받기
    url = input("웹페이지 링크를 입력하세요: ")

    # 본문 내용 가져오기
    text_content = get_text_from_url(url)

    # 결과 출력 (띄어 쓰기 없애기)
    if text_content:
        print(text_content)


