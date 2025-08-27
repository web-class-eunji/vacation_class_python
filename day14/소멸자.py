'''
파이썬에는 쓰레기통이 있기때문에 알아서 필요 없는 객체를 삭제한다.
__del__
메모리 누수
'''

class FileHandler:
    def __init__(self,filename):
        self.file = open(filename,'w')
        print(f"{filename}파일을 열었습니다.")

    def write_data(self,data):
        self.file.write(data)

    def __del__(self):
        self.file.close()
        print("파일을 닫았습니다.")

handler = FileHandler("del_text.txt")
handler.write_data("hello python")
del handler




