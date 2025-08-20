my_dict = {
    "name" : "kelly",
    "age" : 20,
    "city" : "New York"
}

keys = my_dict.keys()
print(keys)

lists = list(my_dict.keys())
print(lists)

values = my_dict.values()
print(values)

values = list(my_dict.values())
print(values)

items = my_dict.items()
print(items)

items = list(my_dict.items())
print(items)

my_dict.update({"age":21, "hobby":"freediving"})
print(my_dict)
#update : 키가 있다면 값을 변경 / 키가 없다면 추가

print(sorted(my_dict))
print(sorted(my_dict.items()))

print(sorted(my_dict, reverse=True))






