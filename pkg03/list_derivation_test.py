'''
author:yb
'''

from math import pi


squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)

squares_lambda = list(map(lambda x: x ** 2, range(10)))
print(squares_lambda)

squares_dev = [x ** 2 for x in range(10)]
print(squares_dev)

list_x_y = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(list_x_y)

vec = [-4, -2, 0, 2, 4]
print([x * 2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])

fruits = [' apple ', ' banana ', ' blackberry ']
print([fruit.strip() for fruit in fruits])

print([(x, x ** 2) for x in range(10)])

second_vec = [[1, 2, 3], [4, 5, 6]]
print([num for elem in second_vec for num in elem])

print([str(round(pi, i)) for i in range(1, 10)])

matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]

print(list(zip(*matrix)))