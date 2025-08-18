'''
커피는 한 잔에 300원
사용자가 돈을 넣으면 커피를 몇 잔 뽑겠냐고 물어볼것
만약 300원 이하의 금액을 투입했다면 300원 이상 투입하라는 문구 출력
입력한 잔 수만큼 받은 돈에서 차감하여 거스름돈을 출력

'''

while True:
    money = int(input("돈을 넣어주세요 (300원 이상 ) : "))
    if money < 300:
        print("300원 이상 넣어주세요!")
        continue

    coffee_price = 300
    #투입된 돈으로 커피를 몇잔 뽑을 수 있는가?
    while True:
        max_coffee = money // coffee_price

        while True:
            coffee_count = int(input(f"몇 잔 뽑으시겠습니까? 최대 {max_coffee}잔 가능 : "))
            if 1 <= coffee_count <= max_coffee:
                break
            print(f"1 ~ {max_coffee} 사이로 입력해주세요")

        money -= coffee_count * coffee_price
        print(f"커피{coffee_count} 잔을 뽑았습니다. 남은 잔돈 : {money}")

        if money < coffee_price:
            choice = input("잔돈이 부족합니다. 추가 투입 하시겠습니까? (1 : 예 / 0 : 아니오) : ")
            if choice == '1':
                add_money = int(input("얼마를 투입하시겠습니까? : "))
                money += add_money
                continue
            elif choice == '0':
                if money > 0:
                    print(f"자판기에 잔돈 {money} 원을 돌려드립니다. 코드를 종료합니다.")
                else:
                    print("자판기를 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 자판기를 종료합니다.")
                break

        more = input("커피를 더 뽑으시겠습니까? (1 : 예 / 0 : 아니오) :")
        if more != '1':
            if money > 0:
                print(f"잔돈 {money}원을 돌려드립니다.")
            break
    break