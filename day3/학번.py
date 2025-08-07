#4자리 학번을 입력받아
# 슬라이싱으로 학년, 반, 번호 추출
# 학년은 첫째자리
# 반은 둘째자리
# 번호는 3-4번
# 1234 -> 1학년 2반 34번

student_id = input("4자리 학번을 입력하세요 : ")
grade = student_id[0]
class_num = student_id[1:2]
student_num = student_id[2:4]
print(f"{grade}학년 {class_num}반 {student_num}번")