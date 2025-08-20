num = 7
nums = [0,1,2,3]
alphabets = ['a','b','c']
boolean_type = [True,False,True]
greetings = ["hello","오늘은 파이썬","8일째"]

mixed_list = [1,"apple",3.14, True]
print(mixed_list)

mixed_list[0] = 2
print(mixed_list)

mixed_list[1] = "mango"
print(mixed_list)

family = ["mother","father","sister","dog"]
print(family[-1])

'''
list[start:end:step]
'''

numbers = [10,20,30,40,50]
print(numbers[0:3])

print(numbers[-2:])

print(numbers[::2])

# numbers[0] = 100
# numbers[1] = 200
# print(numbers)

numbers[:2] = [100, 200]
print(numbers)

numbers[:2] = []
print(numbers)


