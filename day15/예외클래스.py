# age = int(input("나이를 입력해주세요 : "))
# print(f"저의 나이는 {age}살 입니다. ")

try:
    age = int(input("나이를 입력해주세요 : "))
    if(age < 0 or age > 150):
        raise Exception("나이는 0 이상 150 이하로 작성하세요")
except Exception as e:
    print(e)
else:
    print(f"당신은 {age}살 이군요!")
finally:
    print("프로그램을 종료합니다.")

'''
class 클래스이름(부모클래스):
    def __init__(self):
    super().__init__("예외메시지"):
'''

class AgeError(Exception):
    def __init__(self):
        super().__init__("사람의 나이는 0살 이상, 150 미만으로 작성할것")

try:
    age = int(input("나이를 입력하세요 : "))
    if (age < 0 or age > 150):
        raise AgeError
except AgeError as e:
    print(e)
else:
    print(f"당신은 {age}살 이군요!")
finally:
    print("프로그램을 종료합니다.")
