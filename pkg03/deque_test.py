'''
author:yb
'''


from collections import deque

queue = deque(['a', 'b', 'c'])
queue.append('d')
queue.append('e')

print(queue.popleft())
print(queue.popleft())
print(queue)
queue.appendleft("ele")
print(queue)
