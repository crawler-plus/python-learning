'''
author:yb
'''


def ask_ok(prompt, retries = 4, complaint = 'yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'yes'):
            return True
        if ok in ('n', 'no'):
            retries = retries - 1
        if retries < 0:
            raise OSError('invalid user')
        print(complaint)


# ask_ok("do you really want to quit:")
# ask_ok("do you really want to quit:", 2)
# ask_ok("do you really want to quit:", 2, 'yes or no, answer me!')


def f(a, l = None):
    if l is None:
        l = []
    l.append(a)
    return l


print(f(1))
print(f(2))
print(f(3))

