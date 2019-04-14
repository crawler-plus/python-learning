'''
author:yb
'''


def cheeseshop(kind, *args, **keywords):
    for arg in args:
        print(arg)
    print("-----------")
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])


cheeseshop('haha', 'a', 'b', 'c', name='zhangsan', age=10)


def concat(*args, sep="/"):
    return sep.join(args)


print(concat('1', '2', '3'))
print(concat('a', 'b', 'c', sep='.'))

