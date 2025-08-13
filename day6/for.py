for num_list in ["텀블러","스크린","집게핀"]:
    print(num_list)

a = [6,7,8,9,10]
for a_list in a:
    print(a_list)

#안녕하세요 블랙핑그 제니입니다.
black_pink = ["제니","로제","리사","지수"]

for bp_hello in black_pink:
    print(f"안녕하세요 블랙핑크 {bp_hello}입니다.")

for char in "apple":
    print(char)

# 1 ~ 5 정수의 합
'''
range(start,stop,step):
start (선택적): 시작 숫자 ( 생략하면 0 )
stop : 숫자 범위 끝 ( stop에 사용된 값은 포함하지 않음 )
step (선택적): 숫자를 증가시키는 간격 (생갹하면 1) 
'''

for range_for in range(5):
    print(range_for)

for range_for2 in range(2,6):
    print(range_for2)

for range_for3 in range(1,10,2):
    print(range_for3)

for range_for4 in range(10,0,-2):
    print(range_for4)

#1~5 까지의 합 구하기! 합계 : **

total = 0
for range_for5 in range(1,6):
    total += range_for5
print("합계 : ",total)


fruits = ["apple","banana","cherry"]
for fruits_list in range(len(fruits)):
    print(f"인덱스{fruits_list}: {fruits[fruits_list]}")

#range 사용해서 구구단 2단 출력~!

for gugudan2 in range(1,10):
    print(f"2 X {gugudan2} = {gugudan2 * 2}")


