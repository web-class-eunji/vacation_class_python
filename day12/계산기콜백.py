'''
실행함수
x,y, operation

행동함수
더하기 함수
마이너스함수
곱하기함수
나누기(몫)함수
'''

def calculator(x,y,callback):
    return callback(x,y)
    #plus(2,3)

def plus(x,y):
    return x + y

def minus(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x // y

plus_result = calculator(2,3,plus)
print(plus_result)
minus_result = calculator(2,3,minus)
print(minus_result)
multiply_result = calculator(2,3,multiply)
print(multiply_result)
divide_result = calculator(9,3,divide)
print(divide_result)



