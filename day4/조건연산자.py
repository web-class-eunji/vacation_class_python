#피연산자1 if 조건식 else 피연산자2

num1 = 100
num2 = 50

big = num1 if num1 > num2 else num2
print(big)

# 사용자가 좋아하는 숫자가 짝수인지 홀수인지 알아보기!
like_number = int(input("좋아하는 숫자를 입력하세요 : "))
odd = "홀수"
even = "짝수"
result = even if like_number % 2 == 0 else odd
# 어떤 값을 2로 나눈 나머지가 0이라면 짝수

print(result)








