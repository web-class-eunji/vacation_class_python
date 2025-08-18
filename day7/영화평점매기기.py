'''
사용자에게 영화 이름을 입력받은 후
계속 반복하는 while문 시작
영화 평점 입력받기 ( 1 ~ 5 ) 사이로

1~5 사이의 평점이 입력되었다면
    기생충의 평점 : *****

1부터 5 사이의 숫자를 입력하세요! 출력 후 -> 다시 별점 입력 받으러 가기
'''

movie_name = input("영화 이름을 입력하세요 : ")

while True:
    star_input = int(input("영화 평점을 입력하세요(1~5) : "))
    if 1 <= star_input <= 5:
        print(f"{movie_name}의 평점 : " + "⭐" * star_input)
    else:
        print("❗1부터 5 사이의 숫자를 입력하세요!")
        continue
    break