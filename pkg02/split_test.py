'''
author:yb
'''


# 拆分列表
args = [3, 6]
print(list(range(*args)))


# 拆分字典
def print_dict(a, b='staff', c='voom'):
    print(a, ":", b, ":", c)


dict = {"a": "student", "b": "teacher", "c": "parent"}
print_dict(**dict)

