'''
클래스 = 객체를 설계하기 위한 설계도

클래스에는 속성과 행동이 있다.
속성 : 클래스 내부에 정의된 변수 ( 객체가 가지는 데이터 )
메서드 : 클래스 내부에 정의된 함수 (객체가 수행할 수 있는 행동 )

객체 : 클래스라는 설계도를 토대로 만들어진 것
객체는 상태와 행동을 가진다
tv상태  tv행동
가격    볼륨올리기
색상    채널바꾸기
브랜드   전원끄기

행동
1. 능동적행동
    tv를 켜고 / 끄고

2. 수동적행동 (능동적 행동의 결과값)
    tv가 꺼진 상태로 유지됨


class 클래스이름:
    생성자
    메서드

클래스 정의 규칙
1. 이름은 대무낮로 시작한다.
2. 클래스 내부에 함수(메서드)를 추가하여 행동을 정의한다

생성자
1. __init__ 메서드 : 객체가 생성될 때 자동으로 호출되는 생성자이다.
2. 생성자에서는 객체의 초기속성을 설정한다.
3. self는 현재 생성되는 객체 자신을 가리키는 변수로 클래스 내부 메서드에서 항상 첫 매개변수로 전달된다.

'''

class Person:
    def __init__(self,name,age,nationality): #속성
        self.name = name
        self.age = age
        self.nationality = nationality

    #메서드도 항상 self를 첫 매개변수로 받는다.
    def introduce(self):
        print(f"이름 : {self.name}, 나이 :{self.age}, 국적 : {self.nationality}")

person1 = Person("모은지",20,"Korea")
person2 = Person("종종종",32,"USA")
person3 = Person("현민",26,"japan")

print(person1.name)
person1.introduce()

'''
함수
클래스 밖에 정의됨
함수이름()

메서드
클래스 안에서 정의됨
객체이름.메서드이름() *self필요
'''






