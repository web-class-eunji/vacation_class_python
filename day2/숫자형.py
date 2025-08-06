num1 = 10
num2 = -3
num3 = 0
print(num1, num2, num3)

print(num1-num2)

num1 = 100
num3 = 20
print(num1-num3)

print(int(1.9))
print(int('100'))
print(int(True))
print(int(False))
print(int(True + 5))

height = 160.5
weight = 45.6
print(height)
print(weight)

print(height - weight)

x = 2.2
y = 2.8
print(x + y)

first = 3.9
second = 3
print(first * second)

seven = 7.0
three = 3.0
print(seven + three)

print(float(1))
print(float(True))
print(float(False))

'''
곱하기 연산자 : *
더하기 연산자 : +
한 학교에서 학생 한명당 필요한 급식비는 8,000원이다.
선생님은 6,000원이다.
학생 23명과 선생님 2명이 급식을 먹는다.
급식비를 계산하여 출력해주세요.
'''

student_cost = 8000
teacher_cost = 6000
student = 23
teacher = 2

teacher_total_cost = teacher * teacher_cost
student_total_cost = student_cost * student
all_cost = student_total_cost + teacher_total_cost
print("총 급식비는 : ",all_cost," 원 입니다.")


