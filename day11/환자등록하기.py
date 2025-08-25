'''
환자를 담을 빈 리스트 생성
몇명의 환자를 등록할것인지 물어보기

*번째 환자 이름 : 입력받기
*번째 환자 체온 입력받기

비어있는 환자 리스트에 이름과 체온 튜플로 추가하기
'''

patients =[]
q = int(input("몇 명의 환자를 등록하시겠습니까?"))

for i in range(q):
    name = input(f"{i + 1}번째 환자 이름 : ")
    temp = float(input(f"{i + 1}번째 환자 체온 : "))
    patients.append((name,temp))

def check_patients(patients_list,fever=37.5):
    print("환자 발열 검사 결과")
    for user, fever_check in patients_list:
        if fever_check >= fever:
            print(f"{user} : {fever_check} 발열환자입니다.")
        elif fever_check <= 36.0:
            print(f"{user} : {fever_check} 저체온증환자입니다.")
        else:
            print(f"{user} : {fever_check} 정상입니다.")

check_patients(patients)

