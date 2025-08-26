import time

def timer(second,callback):
    #second : 몇초동안 기다릴건지
    #callback: 시간을 기다린 후에 실행할 함수를 콜백으로 받음
    print("타이머 시작")
    print(f"{second}초 뒤에 요청한 함수를 호출합니다.")

    time.sleep(second)
    # time.sleep(5)
    callback()
    #second에 입력한 초를 기다린 후 콜백으로 전달받은 함수를 실행
    print("타이머 종료")

def callback():
    print("3초 뒤 실행될 함수입니다.")

timer(3,callback)
