from sys import path
path.append("D:\\Yakoub Ould bouchiba\\python\\ads\\packages")


from stack.countingStack import CountingStack

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())

