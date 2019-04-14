'''
author:yb
'''

squares = [1, 2, 3, 4, 5]
print(squares)

# 列表切片
print(squares[0])
print(squares[1:3])
print(squares[3:])

# 返回一个全新的列表
other_squares = squares[:]
print(other_squares)

# 列表相加
squares_plus = squares + [6, 7, 8]
print(squares_plus)

# 修改列表元素
squares[3] = 100
print(squares)

# 追加元素
squares.append(80)
squares.append(90)
print(squares)

# 范围操作
squares[1:3] = []
print(squares)

squares[:] = []
print(squares)

# 列表长度
print(len(squares_plus))

# 列表嵌套
list_a = [1, 2, 3]
list_b = ['a', 'b', 'c']
list_c = [list_a, list_b]
print(list_c)
print(list_c[0][1])

