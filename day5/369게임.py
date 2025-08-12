# while, if, continue를 사용하여 369게임 만들기
'''
초기값은 0
반복문을 사용하여 10까지 증가시키는데
0이 증가하다 3의 배수가 되었다면 짝을 출력하고 다음 반복을 실행한다.
'''

num = 0
while num < 10:
    num += 1
    if num % 3 == 0:
        print("짝",end=" ")
        continue
    print(num, end=" ")


'''
시작 숫자는 0
숫자는 30까지 증가!
5의 배수는 출력 X
짝수도 출력 X
27전까지만 출력하기
'''

number = 0
while number <= 30:
    number += 1
    if number % 5 == 0:
        continue
    elif number % 2 == 0:
        continue
    elif number > 27:
        break
    print(number,end=" ")