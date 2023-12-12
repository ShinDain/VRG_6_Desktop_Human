# import requests
# from bs4 import BeautifulSoup
#
# def scrape_weather_and_dust():
#     def create_soup(url):
#         res = requests.get(url)
#         res.raise_for_status()
#         soup = BeautifulSoup(res.text, "lxml")
#         return soup
#
#     print("[오늘의 날씨]")
#     # 날씨 정보 스크랩핑
#     weather_url = 'https://weather.naver.com/today/'
#     weather_soup = create_soup(weather_url)
#
#     location_name = weather_soup.find('strong', {'class': 'location_name'}).text.strip()
#     curr_temp = weather_soup.find("strong", attrs={"class":"current"}).get_text(strip=True)
#     min_temp = weather_soup.find("span", attrs={"class":"lowest"}).get_text()
#     max_temp = weather_soup.find("span", attrs={"class":"highest"}).get_text()
#     cast = weather_soup.find("p", attrs={"class":"summary"}).get_text()
#     cast_string = cast.replace("\n", " ")
#     morning_rainfall = weather_soup.find('span', class_='timeslot', string='오전').find_next('span', class_='rainfall').get_text(strip=True)
#     afternoon_rainfall = weather_soup.find('span', class_='timeslot', string='오후').find_next('span', class_='rainfall').get_text(strip=True)
#
#     print("지역: {}".format(location_name))
#     print("기온: {} | 오늘 {} | 오늘 {}".format(curr_temp, min_temp, max_temp))
#     print("날씨:{}".format(cast_string))
#     print("강수: 오전 {} | 오후 {}".format(morning_rainfall, afternoon_rainfall))
#
#     # 미세먼지 정보 스크랩핑
#     dust_url = 'https://weather.naver.com/air/'
#     dust_soup = create_soup(dust_url)
#
#     fine_dust = dust_soup.find("span", attrs={"class":"value _cnPm10Value"}).get_text()
#     fine_dust_grade = dust_soup.find("span", attrs={"class":"grade _cnPm10Grade"}).get_text()
#     ultra_dust = dust_soup.find("span", attrs={"class":"value _cnPm25Value"}).get_text()
#     ultra_dust_degree = dust_soup.find("span", attrs={"class":"grade _cnPm25Grade"}).get_text()
#
#     print("미세: {}{} 초미세: {}{}".format(fine_dust,fine_dust_grade, ultra_dust, ultra_dust_degree))
#
# # 함수 직접 호출
# scrape_weather_and_dust()


import requests
from bs4 import BeautifulSoup

def scrape_weather_and_dust():
    def create_soup(url):
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        return soup

    print("[오늘의 날씨]")
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8'
    soup = create_soup(url)

    location_name = soup.find("h2", attrs={"class": "title"}).get_text()

    curr_temp = soup.find("div", attrs={"class": "temperature_text"}).get_text(strip=True)
    min_temp = soup.find("span", attrs={"class": "lowest"}).get_text()
    max_temp = soup.find("span", attrs={"class": "highest"}).get_text()

    cast = soup.find("p", attrs={"class": "summary"}).get_text()
    cast_string = cast.replace("\n", " ")

    morning_element = soup.select_one('.weather_inner:has(strong:-soup-contains("오전"))')
    morning_rainfall_element = morning_element.select_one('.rainfall')
    morning_rainfall = morning_rainfall_element.get_text()

    afternoon_element = soup.select_one('.weather_inner:has(strong:-soup-contains("오후"))')
    afternoon_rainfall_element = afternoon_element.select_one('.rainfall')
    afternoon_rainfall = afternoon_rainfall_element.get_text()

    print("지역: {}".format(location_name))
    print("기온: {} | 오늘 {} | 오늘 {}".format(curr_temp, min_temp, max_temp))
    print("날씨:{}".format(cast_string))
    print("강수: 오전 {} | 오후 {}".format(morning_rainfall, afternoon_rainfall))

    # 미세먼지 정보 스크랩핑
    dust_url = 'https://weather.naver.com/air/'
    dust_soup = create_soup(dust_url)

    fine_dust = dust_soup.find("span", attrs={"class":"value _cnPm10Value"}).get_text()
    fine_dust_grade = dust_soup.find("span", attrs={"class":"grade _cnPm10Grade"}).get_text()
    ultra_dust = dust_soup.find("span", attrs={"class":"value _cnPm25Value"}).get_text()
    ultra_dust_degree = dust_soup.find("span", attrs={"class":"grade _cnPm25Grade"}).get_text()

    print("미세: {}{} 초미세: {}{}".format(fine_dust,fine_dust_grade, ultra_dust, ultra_dust_degree))

# 함수 직접 호출
scrape_weather_and_dust()
