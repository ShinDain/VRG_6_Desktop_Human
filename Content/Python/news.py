import requests
from bs4 import BeautifulSoup

# 1
def scrape_politics_headline_news():
    def create_soup(url):
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        return soup

    print("[정치뉴스 헤드라인]")
    url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100"
    soup = create_soup(url)
    news_list = soup.find("ul", class_="sh_list").find_all("li", class_="_cluster_content", limit=5)
    for index, news in enumerate(news_list):
        title_tag = news.select_one('a.sh_text_headline')
        if title_tag:
            title = title_tag.get_text(strip=True)
            link = title_tag['href']
            print("{}. {}".format(index + 1, title))
            print("(링크 : {})".format(link))
        else:
            print("뉴스 {}의 제목을 찾을 수 없습니다.".format(index + 1))


# 2
def scrape_economy_headline_news():
    def create_soup(url):
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        return soup

    print("[경제뉴스 헤드라인]")
    url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101"
    soup = create_soup(url)
    news_list = soup.find("ul", class_="sh_list").find_all("li", class_="_cluster_content", limit=5)
    for index, news in enumerate(news_list):
        title_tag = news.select_one('a.sh_text_headline')
        if title_tag:
            title = title_tag.get_text(strip=True)
            link = title_tag['href']
            print("{}. {}".format(index + 1, title))
            print("(링크 : {})".format(link))
        else:
            print("뉴스 {}의 제목을 찾을 수 없습니다.".format(index + 1))


# 3
def scrape_society_headline_news():
    def create_soup(url):
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        return soup

    print("[사회뉴스 헤드라인]")
    url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=102"
    soup = create_soup(url)
    news_list = soup.find("ul", class_="sh_list").find_all("li", class_="_cluster_content", limit=5)
    for index, news in enumerate(news_list):
        title_tag = news.select_one('a.sh_text_headline')
        if title_tag:
            title = title_tag.get_text(strip=True)
            link = title_tag['href']
            print("{}. {}".format(index + 1, title))
            print("(링크 : {})".format(link))
        else:
            print("뉴스 {}의 제목을 찾을 수 없습니다.".format(index + 1))


# 4
def scrape_culture_headline_news():
    def create_soup(url):
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        return soup

    print("[문화뉴스 헤드라인]")
    url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=103"
    soup = create_soup(url)
    news_list = soup.find("ul", class_="sh_list").find_all("li", class_="_cluster_content", limit=5)
    for index, news in enumerate(news_list):
        title_tag = news.select_one('a.sh_text_headline')
        if title_tag:
            title = title_tag.get_text(strip=True)
            link = title_tag['href']
            print("{}. {}".format(index + 1, title))
            print("(링크 : {})".format(link))
        else:
            print("뉴스 {}의 제목을 찾을 수 없습니다.".format(index + 1))


# 5
def scrape_it_headline_news():
    def create_soup(url):
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        return soup

    print("[IT뉴스 헤드라인]")
    url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
    soup = create_soup(url)
    news_list = soup.find("ul", class_="sh_list").find_all("li", class_="_cluster_content", limit=5)
    for index, news in enumerate(news_list):
        title_tag = news.select_one('a.sh_text_headline')
        if title_tag:
            title = title_tag.get_text(strip=True)
            link = title_tag['href']
            print("{}. {}".format(index + 1, title))
            print("(링크 : {})".format(link))
        else:
            print("뉴스 {}의 제목을 찾을 수 없습니다.".format(index + 1))


# 6
def scrape_world_headline_news():
    def create_soup(url):
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        return soup

    print("[세계뉴스 헤드라인]")
    url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=104"
    soup = create_soup(url)
    news_list = soup.find("ul", class_="sh_list").find_all("li", class_="_cluster_content", limit=5)
    for index, news in enumerate(news_list):
        title_tag = news.select_one('a.sh_text_headline')
        if title_tag:
            title = title_tag.get_text(strip=True)
            link = title_tag['href']
            print("{}. {}".format(index + 1, title))
            print("(링크 : {})".format(link))
        else:
            print("뉴스 {}의 제목을 찾을 수 없습니다.".format(index + 1))


if __name__ == "__main__":
    scrape_politics_headline_news()
    print()
    scrape_economy_headline_news()
    print()
    scrape_society_headline_news()
    print()
    scrape_culture_headline_news()
    print()
    scrape_it_headline_news()
    print()
    scrape_world_headline_news()
