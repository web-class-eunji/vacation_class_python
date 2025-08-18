print('python')
print("12345")

text = "안녕하세용가리~"
print(text[0])
print(text[-1])

# text[-1] = "!"

'''
대소문자 변환
upper() - 대문자로 변환
lower() - 소문자로 변환
capitalize() - 첫 글자만 대문자로 변환

문자열 찾기
fine() - 특정 글자가 어디있는지 찾기
count() - 특정 글자가 몇 번 등장하는지 세기

문자열 변경
replace() - 특정 글자를 다른 글자로 바꾸기

문자열 나누고 합치기
split() - 특정 기준으로 문자열 나누기 ( 리스트로 변환 )
join() - 리스트를 문자열로 합치기

공백 제거하기
strip() - 양쪽 공백 제거
lstrip() - 왼쪽 공백 제거
rstrip() - 오른쪽 공백 제거

문자열이 특정 조건을 만족하는지 확인
startswith() -  특정 문자로 시작하는가
endswith() -  특정 문자로 끝나는가
isdigit() - 숫자로만 이루어져 있는가
isalpha() - 알파벳으로만 이루어져 있는가
'''

money = "money"
print(money.capitalize())

find_text = "fine text"
print(find_text.find("text"))
print(find_text.find("java"))

banana = "banana"
print(banana.count("a"))

replace_text = "I like dog"
print(replace_text.replace("like","love"))