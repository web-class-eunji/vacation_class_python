# 아이디와 비밀번호(숫자)를 입력받음!
# 아이디와 비밀번호가 모두 일치한다면 로그인 되었습니다~
# 아이디가 맞지 않다면 아이디를 다시 입력해주세요
# 비밀번호가 틀렸다면 비밀번호 불일치
# 아이디 비밀번호 불일치 회원가입 하러가기

id = input("아이디를 입력해주세요 :")
pw = int(input("비밀번호를 입력해주세요 : "))

correct_id = "moeunji"
correct_pw = 1234

if id == correct_id and pw == correct_pw:
    print("로그인 되었습니다")
elif id != correct_id and pw == correct_pw:
    print("아이디 불일치")
elif id == correct_id and pw != correct_pw:
    print("비밀번호 불일치")
else:
    print("아이디, 비밀번호 불일치 회원가입 하러가기")
