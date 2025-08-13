import time

start_time = time.time()
end_time = start_time + 20 * 60  # 20분 뒤

while True:
    now = time.time()
    elapsed_minutes = int((now - start_time) // 60)
    print(f"{elapsed_minutes}분 경과")

    # 여기서 먼저 검사!
    if now >= end_time:
        break

    time.sleep(60)

print("20분이 지났습니다!")
