'''
open("파일이름","모드")

모드
1. "r" : 읽기모드
2. "w" : 쓰기모드
3. "a" : 추가모드

파일읽기
1. 변수명.read() : 파일 전체 내용 읽기
2. 변수명.readline() : 파일 한 줄씩 읽기
3. 변수명.readlines() : 파일의 모든 줄을 읽어 리스트로 반환
'''

file = open("text.txt","r")
file_read = file.read()
print(file_read)

file2 = open("text.txt","w")
file2.write("I love icecream")

file2.close()

