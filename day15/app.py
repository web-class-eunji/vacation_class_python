from flask import Flask
from bs4 import BeautifulSoup
from urllib import request

app = Flask(__name__)
weather_url = "https://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20250828.xml"
@app.route("/")
def hello():
    with request.urlopen(weather_url) as response:
        soup = BeautifulSoup(response.read(), "xml")

    html = ["<h1>월간 기온 전망</h1>"]

    for location in soup.select("local_ta"):
        city = location.select_one("local_ta_name").get_text(strip=True)
        # print(f"<h2>{city}</h2><ul>")
        html.append(f"<h2>{city}</h2><ul>")
        for i in range(1, 5):
            base = f"week{i}_local_ta_"
            normal = location.select_one(base + "normalYear").get_text(strip=True)
            rng = location.select_one(base + "similarRange").get_text(strip=True)
            minv = location.select_one(base + "minVal").get_text(strip=True)
            maxv = location.select_one(base + "maxVal").get_text(strip=True)
            sim = location.select_one(base + "similarVal").get_text(strip=True)
            # print(f"{i}주차 | 평균 {normal}도 | 범위 {rng}도 | 최저 {minv}도 | 최고{maxv}도 | 유사사례 {sim}")
            html.append(
                f"<li>{i}주차 | 평균 {normal}도 | 범위 {rng}도 |"
                f"최저 {minv}도 | 최고{maxv}도 | 유사사례 {sim}</li>"
            )
        html.append("</ul>")
    return "\n".join(html)
@app.route("/setting")
def setting():
    return "<h1>설정창으로 들어왔어요!</h1>"

if __name__ == "__main__":
    app.run(debug=True)