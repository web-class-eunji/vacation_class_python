# while문의 처음 조건으로 이동한다.
# while 내에서 continue를 만나면 현재 반복을 건너뛰고 다음 조건을 다시 검사


count = 0
while count < 10:
    print(count)
    count += 1
    if count == 5:
        break


num = 0
while num < 20:
    num += 1
    if num == 5:
        continue
    print(num,end=" ")




