'''
나이와 학생인지 여부에 따라 티켓 가격을 계산하는 프로그램

나이가 20대이고, 학생이라면 성인 요금의 10% 할인된 가격을 적용
나이가 20대인데 학생이 아니라면 가격 할인 X
나이가 20세 미만이라면 어린이요금

학생 여부 판단
20세 미만이라면 False, 아니라면 False/True
'''

#나이 입력받기
age = int(input("나이를 입력해주세요 : "))

#학생 여부 판단
student = False if age < 20 or age >= 30 else bool(int(input("학생인가요? (1:예 / 0:아니오):")))

#요금 설정
#성인 : 10000
#학생 : 6000
adult_price = 10000
child_price = 6000

#할인조건 : 나이가 20대이고, 학생인 경우만 할인
discount = 20 <= age < 30 and student

#기본요금 : 20세 이상이면 성인요금, 아니면 어린이요금
basic_price = adult_price if age >= 20 else child_price

#최종요금
result = basic_price * 0.9 if discount else basic_price

#결과 출력
print("최종 티켓 가격은 : ",int(result),"원 입니다.")
