'''
author:yb
'''

import sys


list = [1, 2, 3, 4]
it = iter(list)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

list2 = [1, 2, 3, 4]
it2 = iter(list2)
for x in it2:
    print(x, end=" ")


print("------------")

list3 = [1, 2, 3, 4]
it3 = iter(list3)  # 创建迭代器对象

while True:
    try:
        print(next(it3))
    except StopIteration:
        sys.exit()