tuple_num = [(1,10),(4,2),(99,6),(5,1),(8,12)]
sorted_tuple1 = sorted(tuple_num)
print(sorted_tuple1)

sorted_tuple = sorted(tuple_num,key=lambda t:t[1])
#sorted(iterable,key=함수) :이터러블인 tuple_num에서 원소를 하나씩 꺼내서 key에 저장된 함수에 보냄
#원소(1,10),(4,2) 등등등
# lambda index(1,10):index[1]

print(sorted_tuple)