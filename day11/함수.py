'''
1. 반복적인 코드 제거 및 재사용성 향상
2. 어떤 기능을 수행하는 코드인지 한 눈에 파악 가능 ( 가독성이 좋아짐 -> 유지보수 )
3. 오류 추적(디버깅) 효율적

def 함수이름():
    코드
'''

def hello():
    print("안녕하세요")
    print("저는 안나입니다.")
    print("엘사 동생이에요")

hello()

'''
int hello(){
print("안녕하세요");
print("저는 안나입니다.")
    print("엘사 동생이에요")
    return 0;
}
'''

animals = ["강아지","고양이","햄스터","곰","기린"]
index = 0

def change_animal():
    global index
    if index >= len(animals):
        index = 0
    print(f"동물을 {animals[index]}로 변경합니다.")
    index += 1

change_animal()
change_animal()
change_animal()
change_animal()
change_animal()
change_animal()






