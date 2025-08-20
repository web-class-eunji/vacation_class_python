fruit_colors = {
    "red" : "apple",
    "yellow" :"banana",
    "purple" : "blueberry"
}

for i in fruit_colors:
    print(i)

sport_star = {
    "축구" : "손흥민",
    "피겨" : "김연아",
    "수영" : "박태환",
    "펜싱" : "박상영"
}

for i,star in sport_star.items():
    print(i)
    print(star)

sport_list = list(sport_star.keys())
print(sport_list)

sport_list.append("농구")
print(sport_list)

for i in sport_star:
    print(i)

sport_star["농구"] = "서장훈"
print(sport_list)
print(sport_star.items())