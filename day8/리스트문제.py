students = [
    ["kim","95","  Pizza  "],
    ["lee","80","pasta"],
    ["park","?","   piano"],
    ["choi","77","pancake"]
]

#for문을 사용하여 리스트에 접근할것
print("1) 변수를 만들어서 이름 첫 글자만 대문자로 보여주기")
for i in students:
    name = i[0].capitalize()
    print(name)
print("2) 점수가 숫자인 학생들의 평균(정수) 구하기 ( 숫자가 아니면 제외 )")
total = 0
count = 0
for i in students:
    score = i[1]
    if score.isdigit():
        total += int(score)
        count += 1
avg = total // count if count > 0 else 0
print("유효인원 : ",count, "평균 : ",avg)
