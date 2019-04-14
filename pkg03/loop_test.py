'''
author:yb
'''


dict = {'first_key': 'first_value', 'second_key': 'second_value'}
for k, v in dict.items():
    print(k, v)

for i, v in enumerate(['a', 'b', 'c', 'd']):
    print(i, v)

questions = ['name', 'color']
answers = ['yb', 'yellow']
for q, a in zip(questions, answers):
    print("what is your {0}? It is {1}".format(q, a))

for i in reversed(range(1, 10 , 2)):
    print(i)

basket = ['apple', 'apple', 'banana', 'orange', 'pear']
for f in sorted(set(basket)):
    print(f)