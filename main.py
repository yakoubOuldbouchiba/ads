from sys import path
path.append("D:\\Yakoub Ould bouchiba\\python\\ads\\packages")


from stack.countingStack import CountingStack
from custom_queue.queue import Queue
from custom_queue.super_queue import SuperQueue

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")