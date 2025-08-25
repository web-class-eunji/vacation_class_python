'''
정해진 id, pw있음
로그인이라는 함수를 만들것 ( 매개변수로 아이디와 패스워드를 받을것 )
정해진 id 와 매개변수로 받은 id같다면  -> pw검사할 수 있음
정해진 pw와 매개변수로 받은 pw가 같다면 -> 로그인 되었습니다.
정해진 pw와 매개변수로 받은 pw가 다르다면 -> 비밀번호가 일치하지 않습니다.
정해진 id 와 매개변수로 받은 id다르다면 -> 아이디가 일치하지 않습니다.
'''

set_id = "moeunji"
set_pw = 1234

def login(id,pw):
    if set_id == id:
        if set_pw == pw:
            print("로그인 되었습니다")
        else:
            print("비밀번호가 일치하지 않습니다")
    else:
        print("아이디가 일치하지 않습니다")

user_id = input("아이디를 입력해주세요 : ")
user_pw = int(input("비밀번호를 입력해주세요 : "))

login(user_id,user_pw)