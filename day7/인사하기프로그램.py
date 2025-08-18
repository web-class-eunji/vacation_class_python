'''
정수를 입력받아서 입력받은 횟수만큼 *번째 안녕하세요
0보다 이하의 수가 입력되었다면 잘못된 입력입니다. 출력
'''

num = int(input("숫자를 입력하세요 : "))

if num <= 0:
    print("잘못된 입력입니다. 1이상의 수를 입력하세요~!")
else:
    for hello in range(num):
        print(f"{hello + 1}번째 안녕하세요")