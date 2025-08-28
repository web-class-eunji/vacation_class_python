'''
터미널 : pip install 모듈 이름
pip install Flask ( 웹서버 ) / Django
pip install beautifulest4 / requests- 웹에서 데이터 불러와서 분석하기
pip install tensorflow (인공지능) / scikit-learn
cv2 / pillow
python midi

1. 학습,연구
2. 악용X
'''

from bs4 import BeautifulSoup
from urllib import request

weather_url = "https://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20250828.xml"
data = request.urlopen(weather_url)

with request.urlopen(weather_url) as response:
    soup = BeautifulSoup(response,"xml")

for location in soup.select("local_ta"):
    city = location.select_one("local_ta_name").get_text(strip = True)
    print(f"\n{city}")

    for i in range(1,5):
        base = f"week{i}_local_ta_"
        normal = location.select_one(base + "normalYear").get_text(strip = True)
        rng = location.select_one(base + "similarRange").get_text(strip=True)
        minv = location.select_one(base + "minVal").get_text(strip=True)
        maxv = location.select_one(base + "maxVal").get_text(strip=True)
        sim = location.select_one(base + "similarVal").get_text(strip=True)
        print(f"{i}주차 | 평균 {normal}도 | 범위 {rng}도 | 최저 {minv}도 | 최고{maxv}도 | 유사사례 {sim}")




