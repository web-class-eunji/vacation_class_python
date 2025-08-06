a = "apple"
first_char = a[0]
third_char = a[3]
print(first_char)
print(third_char)

last_char = a[-1]
print(last_char)
second_char = a[-4]
print(second_char)

#문자열 슬라이싱
#변수명[start:stop:step] : 문자열 슬라이스 구조
'''
start : 슬라이싱을 시작할 위치를 정한다. (생략하면 0!)
stop : 슬라이싱을 종료할 위치를 정한다. (* 출력하고싶은 단어의 마지막 인덱스번호 + 1을 하여 작성 )
step : 증감폭(인덱스의 증가 또는 감소 지정, 기본값 1 - 생략하면 1)
'''

text = "I Love Pasta"
slicing1 = text[2:6]
print(slicing1)

slicing2 = text[7:12]
print(slicing2)

slicing_step = text[7:12:2]
print(slicing_step)

first_lost = text[:6]
print(first_lost)

last_lost = text[6:]
print(last_lost)
