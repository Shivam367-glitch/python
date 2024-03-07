from queue import Queue
from collections import deque


# print(dir(deque))

# q=Queue()
# q.put(1)
# q.put(2)
# print(q.queue)
# print(dir(collections.deque))


# double ended queue(deque)
d=deque()
d.append(1)
d.append(2)
d.append(3)
d.appendleft(-1)
d.appendleft(-2)

# reverse the deque
print(d.reverse ())

#count how may time 2 present in deque
print(d.count(2))

#clear the deque
print(d.clear())