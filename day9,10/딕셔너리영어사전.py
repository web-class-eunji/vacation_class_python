english_dict = {
    "flower" : "꽃",
    "food" : "음식",
    "sky" : "하늘",
    "fish" : "물고기"
}

user_word = input("영어 단어를 입력해주세요 :")
#in 연산자를 통해 입력한 단어가 english_dict에 있는지 확인 있다면 출력해주기
if user_word in english_dict:
    print(f"{user_word} : {english_dict[user_word]}")
else:
    print(f"{user_word} 는 사전에 없습니다.")
    add_values = input("단어의 뜻을 입력해주세요 : ")
    english_dict[user_word] = add_values
    print(f"{user_word} : {english_dict[user_word]}(사전에 추가되었습니다!) ")

