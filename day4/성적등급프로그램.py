#사용자의 점수를 입력받아
#90점 이상이라면 A학점
#80점 이상이라면 B학점
#70점 이상이라면 C학점
#60점 이상이라면 D학점
#위 조건에 부합하지 않는다면 F학점 재시험!

score = int(input("점수를 입력해주세요 : "))

if score >= 90:
    print("A학점 참 잘했어요!")
elif score >= 80:
    print("B학점")
elif score >= 70:
    print("C학점")
elif score >= 60:
    print("D학점")
else:
    print("F학점으로 재시험 당첨~")



