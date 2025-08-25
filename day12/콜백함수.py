def greet(name):
    print(f"안녕하세요 {name}님!")

greet("민수")

def callback_functiuon(callback):
    print("이제 콜백함수 실행할거임")
    callback("이수근")

callback_functiuon(greet)


def hello(name):
    print(f"안녕,{name}!")

hello("봄")

# callback : 실행할 다른 함수(이름을 임의로 정해줌)
#name : 이름을 받을것
def hello_callback(callback,name):
    callback(name)#hello(name)

hello_callback(hello,"은지")

def dinner(name):
    print(f"{name}님은 저녁을 먹었습니다.")

def lunch(name):
    print(f"{name}님은 점심을 먹었습니다.")

def eating_function(eat,name):
    eat(name)
    #밥을 먹는 함수!!
    #dinner(name)

eating_function(dinner,"은지")
eating_function(lunch,"현종")





