'''
author:yb
'''


list = [1, 2, 3, 4, 5, 6, 7, 7]

print(list)
print(list.count(2), list.count(7), list.count(9))
print(list.index(2))

list.remove(6)
print(list)

list.reverse()
print(list)

list.sort()
print(list)

ele = list.pop()
print(ele)
print(list)