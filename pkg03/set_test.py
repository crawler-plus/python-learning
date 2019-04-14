'''
author:yb
'''


basket = {'apple', "orange", "apple", "pear", "orange", "banana"}
print(basket)

print("apple" in  basket)
print("dog" in basket)

a = set("abcdeabcde")
b = set("bcdef")
print(a)
print(b)
print(a - b)
print(a | b)
print(a & b)

print("-----------------")

set_defer = {x for x in 'abcdeabcde' if x not in 'abc'}
print(set_defer)