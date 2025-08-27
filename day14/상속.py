'''
상속이란
부모클래스(슈퍼클래스)의 속성과 메서드를 물려받아 사용할 수 있도록 만드는 개념
'''

class Animal:
    def __init__(self,type):
        self.type = type

    def make_sound(self):
        print("소리를냅니다!")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__("강아지")
        # 부모클래스의 생성자를 불러서 self.type = "강아지"
        # super() 부모 클래스의 속성과 기능을 가져다 쓰겠다!
        # 그런데 가져다 쓰려고 보니까 type을 설정하는 코드가 있네? 가져다써야지!
        self.name = name
        self.breed = breed

    def make_sound(self):
        print("멍멍 왈왈")
        #오버라이딩(재정의)
        #부모클래스에서 정의한 메서드를 자식클래스가 다시 정의하는것
        #부모것도 있는데 난 내가 바꿔서 쓸래

class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__("고양이")
        # 부모클래스의 생성자를 불러서 self.type = "강아지"
        # super() 부모 클래스의 속성과 기능을 가져다 쓰겠다!
        # 그런데 가져다 쓰려고 보니까 type을 설정하는 코드가 있네? 가져다써야지!
        self.name = name
        self.breed = breed

    def make_sound(self):
        print("야옹 먕먕")


dog = Dog("봄이","말티푸")
print(f"{dog.name}는 {dog.breed}이며, {dog.type} 입니다.")
dog.make_sound()

cat = Cat("오레오","턱시도냥이")
print(f"{cat.name}는 {cat.breed}이며, {cat.type} 입니다.")
cat.make_sound()

