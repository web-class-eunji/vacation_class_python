'''

람다함수 = 익명함수
def 함수이름(매개변수):
    return 결과
============================
lambda 매개변수:return값
'''

def add(x,y):
    return x + y

print(add(5,1))

lambda_add = lambda x,y:x+y
print(lambda_add(5,5))

numbers = list(range(1,21))
print(numbers)

even_numbers = list(filter(lambda x:x % 2 == 0,numbers))
#filter(함수, iterable) : 조건에 맞는 요소만 걸러주는 함수
# filter는 리스트를 뽑아 반환해주는 것이 아니라 필요할 때 하나씩 꺼내서 쓸 수 있도록 보관
# for i의 역할
#iterable : 검사할 데이터 ( 리스트, 튜플 )

#lambda x:x % 2 == 0
# x : 매개변수
# x % 2 == 0 -> 리턴값

print(even_numbers)


