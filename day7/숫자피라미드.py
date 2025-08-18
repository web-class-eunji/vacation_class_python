'''
2중 for문과 range를 사용하여
1
22
333
4444
55555
이렇게 출력해보세요~!
'''

n = 5
for i in range(1,n + 1):
    for j in range(i):
        print(i, end=" ")
    print()



