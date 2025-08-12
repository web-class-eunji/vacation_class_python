count = 0
while count <= 100: #조건이 참인지 검사
    print(count)
    #count = count + 1
    count += 1

#10부터 5까지 감소하기!!
count2 = 10
while count2 >= 5:
    count2 -= 1
    print(count2)
    #count2 -= 1

'''
우리가 가진 돈 : 5000
아이스크림 : 1000
아이스크림을 2번 사먹을거임
아이스크림을 1번 사먹었다! 남은 돈 : ??원
아이스크림을 2번 사먹었다! 남은 돈 : ??원
'''

money = 5000
icecream_price = 1000
icecream_count = 1

while icecream_count <= 2:
    money -= icecream_price
    print(f"아이스크림을{icecream_count}번 사먹었다! 남은 돈은 {money}원ㅜㅠ")
    icecream_count += 1

num = 0
while num < 3:
    print(num)





