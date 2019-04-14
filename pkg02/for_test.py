'''
author:yb
'''

words = ['cat', 'dog', 'rabbit', 'tiger']
for w in words:
    print(w, len(w))

# 在迭代过程中修改迭代序列不安全，如果想要修改迭代的序列，可以迭代它的复本
for w in words[:]:
    if len(w) > 5:
        words.append(w)
print(words)