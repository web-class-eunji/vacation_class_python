'''
비행기는 총 3대 운항
프로그램을 실행하면 ( 1번째 비행기 탑승 준비! ) 출력
비행기는 여권을 가진 사람 2명이 탑승하면 출발함
승객에게 질문 : *번째 고객님 여권이 있나요? (yes : 1, no :0)
여권이 없다면 여권이 없어요! 다음 승객 기다리기.... 출력 후
다음 승객에게 다시 여권 유무 물어보기
여권이 있는 승객이 나타나면 *번째 승객이 탑승했어요! 출력 후
한명밖에 안 탔으니까 다시 여권 유무 묻기
여권을 가진 승객 2명이 다 채워졌다면 비행기 출발 후 다음 비행기 운항 ( 2번째 비행기 탑승 준비!)
while 2개 / if 1개 --> continue 1개
'''

flight = 1
while flight <= 3:
    print(f"{flight}번째 비행기 탑승 준비!")
    passenger = 1
    count = 0
    while count < 2:
        passport = int(input(f"{passenger}번째 고객님 여권이 있나요? [yes:1 / no:0]"))

        #여권이 없다면?
        if passport == 0:
            print("여권이 없어요! 다음 승객 기다리기...")
            passenger += 1
            continue

        print(f"{passenger}번째 승객이 탑승했어요!🧑")
        passenger += 1
        count += 1
    print("비행기 출발!✈️")
    flight += 1
    print()