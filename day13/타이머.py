import time

start_time = time.time()
#1970 1월 1일 0시 0분 0초 ~ 지금까지 흐른 시간을 초단위로 반환
print(time.time())

end_time = start_time + 4 * 60
# 5분 = 5 * 60 = 300초
# 1756196122 + 300

while True:
    now = time.time()
    minutes = int((now - start_time) // 60)
    #now - start_time : 시작 이후 지나간 초
    # now = time.time()
    # start_time = time.time()
    #start_time : 프로그램을 돌리기 시작한 시간 (기준점)
    #now : 반복문이 돌면서 지체될텐데 그 시간을 담아주는 진짜 지금의 시간

    print(f"{minutes}분 경과")
    time.sleep(60)
    #sleep : 인자를 초단위로 받는다.

    if now >= end_time:
        break

print("5분이 지났습니다!")