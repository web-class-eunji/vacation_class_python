list_in_list = [1,[2,3],"hello",[True,False]]
print(list_in_list)
print(list_in_list[1][1])

python_class = [
    ["철수","영희","민수"], #1조
    ["지수","현우","나영"], #2조
    ["동현","수진","호영"]  #3조
]

for python_class_for in python_class:
    for student in python_class_for:
        print(student)

#1조 출력
print(python_class[0])
#2조 출력
print(python_class[1])
#3조 출력
print(python_class[2])
#3조에 있는 수진이 출력
print(python_class[2][1])
#민수 출력
print(python_class[0][2])
#지수가 로제로 이름을 개명한 후 2조 출력
python_class[1][0] = "로제"
print(python_class[1])

#colors라는 리스트에는 red orange green yello
# for문을 사용하여 colors라는 리스트를 돌기!
colors = ["red","orange","green","yello"]
for color_for in colors:
    print(color_for, end=" ")



