import time

def printWays(n, max):
    def helper(path, last, n):
        if n == 0:
            print(path)
        if n > 0:
            for i in range(1, max):
                if i is not last:
                    path.append(i)
                    helper(path, i, n - i)
                    path.pop()
    helper([], None, n)

def printWays2(n, max):
    def helper(path, last, n):
        if last:
            path = path + [last]
        if n == 0:
            print(path)
        if n > 0:
            for i in range(1, max):
                if i is not last:
                    helper(path, i, n - i)
    helper([], None, n)

start = time.time()
printWays(40, 4)
print("time:", time.time() - start)