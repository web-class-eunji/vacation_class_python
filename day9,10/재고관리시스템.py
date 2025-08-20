inventory = {
    "꿀꽈배기" : 10,
    "매운새우깡" : 3,
    "오징어집": 0,
    "프링글스": 5,
}

#재고가 0이라면 재고가 없습니다!
# 5개 미만이라면 재고가 부족합니다.
# 위 조건에 걸리지 않는다면 재고충분!

for name,stock in inventory.items():
    if stock == 0:
        print(f"{name} 재고가 없습니다!")
    elif stock < 5:
        print(f"{name} 재고가 부족합니다. 현재 {stock}개 남음")
    else:
        print(f"{name} 재고가 충분합니다. 현재 {stock}개")



