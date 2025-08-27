class Mom:
    def make_Kimchi_stew(self):
        print("엄마 레시피 : 김치 + 돼지고기 + 파 넣고 끓이기")

class Me(Mom):
    def make_Kimchi_stew(self):
        #자식클래스에서 엄마와 똑같은 이름의 메서드를 새로 정의하면 자동으로 오버라이딩이됨
        # print("내 레시피 : 김치 + 돼지고기 + 양파 넣고 끓이기")

        super().make_Kimchi_stew()
        print("엄마의 레시피에 나는 양파를 더 추가해서 끓여먹어야지~")

mom = Mom()
me = Me()

mom.make_Kimchi_stew()
me.make_Kimchi_stew()