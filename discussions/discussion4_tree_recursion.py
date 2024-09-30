def index(keys, values, match):
    """
    >>> index([7, 9, 11], range(30, 50), lambda k, v: v % k == 0)
    {7: [35, 42, 49], 9: [36, 45], 11: [33, 44]}
    """
    return {key: [val for val in values if match(key, val)] for key in keys}

#print(index([7, 9, 11], range(30, 50), lambda k, v: v % k == 0))

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    return (lambda f: lambda x: f(f)(x))(lambda f: lambda n: 1 if n == 0 else n * f(f)(n - 1))(m + n - 2)
    fact = (lambda f: lambda x: f(f)(x))(lambda f: lambda n: 1 if n == 0 else n * f(f)(n - 1))
    return fact(m + n - 2) // (fact(m - 1) * fact(n - 1)) 
print(paths(2, 2)) 
print(paths(3, 3)) #6
print(paths(5, 7))

def max_product(s):
    """Return the maximum product of non-consecutive elements of s.

    >>> max_product([10, 3, 1, 9, 2])   # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5])  # 5 * 5 * 5
    125
    >>> max_product([])                 # The product of no numbers is 1
    1
    """
    #either starts from index 0 or index 1 which is why we need a helper otherwise
    #in every recursive call you would also start from the second elem which is not allowed
    #since you have to skip
    """def maxProductHelper(s):
        if len(s) == 0:
            return 1
        return s[0] * max(maxProductHelper(s[2:]), maxProductHelper(s[3:]))
    return max(maxProductHelper(s), maxProductHelper(s[1:]))"""
    if len(s) == 0:
        return 1
    elif len(s) == 1:
        return s[0]
    else:
        return s[0] * max(max_product(s[2:]), max_product(s[3:]))
#print(max_product([10, 3, 1, 9, 2]))

    

def sums(n, m):
    """Return lists that sum to n containing positive numbers up to m that
    have no adjacent repeats.

    >>> sums(5, 1)
    []
    >>> sums(5, 2)
    [[2, 1, 2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    >>> sums(5, 5)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
    >>> sums(6, 3)
    [[1, 2, 1, 2], [1, 2, 3], [1, 3, 2], [2, 1, 2, 1], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    return (lambda f: lambda x, k: f(f)(x, k))(lambda f: lambda n, m: [] if n < 0 else [[]] if n == 0 else [[k] + rest for k in range(1, m + 1) for rest in f(f)(n - k, m) if rest == [] or k != rest[0]])

    if n < 0:
        return []
    if n == 0:
        sums_to_zero = []     # The only way to sum to zero using positives
        return [sums_to_zero] # Return a list of all the ways to sum to zero
    result = []
    for k in range(1, m + 1):                               #we succeeded/returned [[]]
        result = result + [[k] + rest for rest in sums(n-k, m) if rest == [] or k != rest[0]] #true if we return [[]]
    return result
#sums(6, 3)

# list = [1, 2, 3, 4, 5]
# f = lambda x: x * x
# map = {item : f(item) for item in list}
# print(map)

def fibonacci(n):
    memo = [0, 1]
    def helper(n, memo):
        if len(memo) > n: #must be one greater
            return memo[n]
        value = helper(n - 1, memo) + helper(n - 2, memo)
        memo.append(value)
        return value
    return helper(n, memo)

#print(fibonacci(6))

