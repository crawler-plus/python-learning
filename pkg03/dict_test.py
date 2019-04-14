'''
author:yb
'''


tel = {'yb': 110, 'yb2': 119}
print(tel)
tel['yb'] = 120
print(tel)

del tel['yb']
print(tel)

print(list(tel.keys()))
print(list(tel.values()))
print('yb' in tel)
print("yb" not in tel)

my_dict = dict([('a', 100), ('b', 120), ('c', 140)])
print(my_dict)

my_dict_infer = {x: x**2 for x in (1, 3, 5)}
print(my_dict_infer)

my_dict_keyword = dict(apple=1, banana=2, pear=3)
print(my_dict_keyword)

