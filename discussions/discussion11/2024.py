import inspect

def f(x):
    return x - 1

def g(x):
    return 2 * x

def h(x, y):
    return int(str(x) + str(y))

funcs = [g, f]

def findWays(n): # n: # OF FUNCITON CALLS
    if n == 0:
        return {5:[[]]}
    li = {}
    for key, paths in findWays(n - 1).items(): #key val pairs
        #5
        # [] or [['g', 'f'], ['f', 'g']]
        for f in funcs:
            if f(key) not in li:
                li[f(key)] = []
            li[f(key)].extend([[f.__name__] + path for path in paths]) #if paths is empty we have nothing to iterate
    return li

print(list(filter(lambda x: x[0] == 10, findWays(6).items()))) #x is the key
# print(list(filter(lambda x: x == x,findWays(6))))

def findWays2(n): # n is number of function calls
    if n == 0: # out of function calls, return 5
        return {5:[[]]}
    li = {}
    for key, paths in findWays2(n - 1).items(): #key val pairs
        #5
        # [] or [['g', 'f'], ['f', 'g']]
        for f in funcs:
            if f(key) not in li:
                li[f(key)] = []
            li[f(key)].extend([[f.__name__] + path for path in paths]) #if paths is empty we have nothing to iterate
    return li


#****************************************************************


class Number:
    def __init__(self, n):
        self.value = n
    def __str__(self):
        return str(self.value)
    def calls(self):
        return 0
    
functions = [h, g, f]

class Call: # a call stores a series of functions, we can check if each series yields a specific value
    def __init__(self, f, operands):
        self.f = f
        self.operands = operands #operands is a list
        self.value = f(*[e if isinstance(e, int) else e.value for e in operands])

    def __str__(self): #return the function name with its operands inside
        return f'{self.f.__name__}({",".join(map(str, self.operands))})'
    
    def calls(self):
        return 1 + sum(o.calls for o in self.operands)
    
def dynamic(args_left, f, n, getArgs=False):
    if args_left == 0:  # Base case: All arguments processed
        yield []
    if n > 0 and args_left > 0 and not getArgs:
        for i in range(0, n): #iterate through the number of calls used on this arg
            for arg in finalWays(i): #get the curr arg
                for func in functions: #get the next function
                    for next_args in list(dynamic(args_left - 1, func, n - i, getArgs=True)):
                        yield Call(f, [arg] + next_args)
    if n > 0 and args_left > 0 and getArgs:
        for i in range(0, n): #iterate through the number of calls used on this arg
            for arg in finalWays(i): #get the curr arg
                for func in functions:
                    for next_args in list(dynamic(args_left - 1, func, n - i, getArgs=True)):
                        yield [arg] + [] if next_args == [] else [next_args]

def finalWays(n):
    if n == 0:
        yield Number(5)
    for f in functions: # dynamic gets the arguments to the function, yielding all
        yield from dynamic(len(inspect.signature(f).parameters), f, n) 

#x = list(finalWays(3))
print([{e.value: e.__str__()} for e in finalWays(8) if e.value == 2024])

def ways(n):
    if n == 0:
        yield Number(5)
    #ideally we can plug into any function the result of any other 
    if n > 0:
        for operand in ways(n - 1): #single arg
            for f in functions: # f might take multiple arguments
                try:
                    yield Call(f, [operand])
                except TypeError:
                    pass # do nothing
        for k in range(n): #k is how many times called first func
            for first in ways(k):
                for second in ways(n - k - 1):
                    if first.value < 0 or second.value < 0:
                        continue
                    yield Call(h, [first, second])
        

print([{e.value: e.__str__()} for e in ways(7) if e.value == 2024])

