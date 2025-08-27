'''
1. 에러(우리가 잘못 입력한것)
2. 예외(사용자의 입력 오류에 따라 발생)
'''

# print(7/0)

# num1 = int(input("첫 번째 정수를 입력하세요 : "))
# num2 = int(input("두 번째 정수를 입력하세요 : "))
# # print(f"{num1} / {num2} 의 결과는 : {num1 / num2} 입니다.")
#
# if num2 == 0:
#     print("0으로 나눌 수 없습니다.")
# else:
#     print(f"{num1} / {num2} 의 결과는 : {num1 / num2} 입니다.")


'''
BaseExceprion: 최상위 예외클래스 
Exception : 대부분 예외클래스의 슈퍼클래스
ArithmeticError : 산술연산오류
    OverflowError : 결과가 너무 커서 표현할 수 없음
    ZeroDivisionError: 0 으로 나누려고 할 때 발생
    FloatingPointError : 실수연산에서 오류
AttributeError : 잘못된 속성 참조
EOFError : 파일에서 더이상 읽을 데이터가 없을때
Module NotFoundError : import할 모듈이없을때
FileFoundError:존재하지 않는 파일 찾으려고 할 때
IndexError : 잘못된 인덱스 사용
NameError : 변수를 선언하지 않고 사용
SyntaxError : 코드 문법 어기면 나옴
TypeError : 서로 다른 데이터 타입끼리 연산하려고 하면 발생
ValueError : 계산하려는 데이터값 오류
'''

try:
    num1 = int(input("첫 번째 정수를 입력하세요 : "))
    num2 = int(input("두 번째 정수를 입력하세요 : "))
    print(f"{num1} / {num2} 의 결과는 : {num1 / num2} 입니다.")
except ArithmeticError:
    print("산술 연산 예외발생")
except ValueError:
    print("입력값을 확인하세요.예외발생")

try:
    list = [1,2,3,4]
    print(list[1])
except IndexError:
    print("인덱스 범위를 벗어났습니다.")