'''
붕어빵 클래스를 만든다.
생성자는 어떤맛인지, 개수
making메서드 **맛 붕어빵 **개 나왔습니다!
'''

class FishBread:
    def __init__(self,taste,count):
        self.taste = taste
        self.count = count

    def making(self):
        print(f"{self.taste}맛 붕어빵 {self.count}개 나왔습니다:)")

fish_bread1 = FishBread("슈크림",3)
fish_bread2 = FishBread("팥",2)
fish_bread3 = FishBread("김치",1)

fish_bread1.making()
fish_bread2.making()
fish_bread3.making()