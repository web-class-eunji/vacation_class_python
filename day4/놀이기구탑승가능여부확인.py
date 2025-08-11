# 사용자에게 나이를 입력받음
# 사용자에게 키를 입력받음
# 정수로 입력받음

# 키가 120이상, 나이가 10살 이상이어야만 탑승 가능
# 탑승 여부는 True / False로 구분

height = int(input("키를 입력하세요 : "))
age = int(input("나이를 입력하세요 : "))

can_ride = height >= 120 and age >= 10
print("놀이기구를 탈 수 있나요?",can_ride)




