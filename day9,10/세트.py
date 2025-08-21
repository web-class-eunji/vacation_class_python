'''
변수명 = {요소1, 요소2, 요소3}
'''

'''
리스트 : [ ]

딕셔너리 : {
    키 : 값
}

튜플 : ( )

세트 : { }

'''

str = "apple"
list = [1,2,3]
tuple = (1,2,3)

set_str = set(str)
set_list = set(list)
set_tuple = set(tuple)
print("set_str : ",set_str)
print("set_list : ",set_list)
print("set_tuple : ",set_tuple)

str_banana = "banana"
set_banana = set(str_banana)
print(str_banana[0])
# print(set_banana[0])


# list_banana = list(set_banana)
# tuple_banana = tuple(set_banana)

str_random = "asgvjfjmsdfmcloawehfick"
str_random = set(str_random)
print(str_random)

sorted_list_change = sorted(set(str_random))
print(sorted_list_change)

print(str_random)

