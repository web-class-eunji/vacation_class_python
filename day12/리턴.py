def plus(a,b):
    return a + b

sum = plus(10,20)
print(sum)

print(plus(10,20))

def multiply(num):
    result = num * 7
    return result

print(multiply(3))

def bools_check():
    return True

print(bools_check())


#어떤 값을 넘겼을 때 리턴과 매개변수를 사용해서 7의 배수인지 아닌지 판단해주는 함수 만들기
# True / False

def check_divide_seven(num2):
    if num2 % 7 == 0:
        return True
    else:
        return False

print(check_divide_seven(14))

