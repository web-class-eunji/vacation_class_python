class Person:
    def __init__(self):
        print("생성자가 호출됨!")

class Person2:
    def say_hello(self):
        print("안녕하세요!")

p1 = Person()

p2 = Person2()
p2.say_hello()