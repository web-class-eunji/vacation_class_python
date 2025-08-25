'''
 국어, 영어, 수학 점수를 다 더하는 함수를 만들것
 total <- 만들어서 더해주기

 avg
 avg return 하는 함수 만들기~!
'''

def calc_score(kor,eng,math):
    total = kor + eng + math
    avg = total / 3
    return avg

def grade_function(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

kor = int(input("국어점수를 입력하세요 : "))
eng = int(input("영어점수를 입력하세요 : "))
math = int(input("수학점수를 입력하세요 : "))

average = calc_score(kor,eng,math)
grade = grade_function(average)

print(f"평균 점수 : {average:.2f}")
print(f"최종 학점 : {grade}")


