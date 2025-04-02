def count_calls(f):
    def count(*args):
        count.count += 1
        return f(*args)
    count.count = 0
    return count

def memo(f):
    m = {}
    def memoized(*args):
        if args not in m:
            m[args] = f(*args)
        return m[args]
    return memoized

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


fib = memo(fib)
fib = count_calls(fib)  # Reassigning fib to its decorated version
fib.count = 0
print(fib(32))
print(f"fib was called {fib.count} times")

from linkedlist import *

################################################

def strange_loop():
    """Return a Link s for which s.rest.first.rest is s.

    >>> s = strange_loop()
    >>> s.rest.first.rest is s
    True
    """
    "*** YOUR CODE HERE ***"
    link = Link(2)
    link.first = link
    link.rest = link
    return link


def sum_rec(s, k):
    """Return the sum of the first k elements in s.

    >>> a = Link(1, Link(6, Link(8)))
    >>> sum_rec(a, 2)
    7
    >>> sum_rec(a, 5)
    15
    >>> sum_rec(Link.empty, 1)
    0
    """
    # Use a recursive call to sum_rec; don't call sum_iter
    "*** YOUR CODE HERE ***"
    if k == 0 or s is Link.empty:
        return 0
    else:
        return s.first + sum_rec(s.rest, k - 1)

def sum_iter(s, k):
    """Return the sum of the first k elements in s.

    >>> a = Link(1, Link(6, Link(8)))
    >>> sum_iter(a, 2)
    7
    >>> sum_iter(a, 5)
    15
    >>> sum_iter(Link.empty, 1)
    0
    """
    # Don't call sum_rec or sum_iter
    "*** YOUR CODE HERE ***"
    sum = 0
    while k > 0 and s is not Link.empty:
        sum += s.first
        s, k = s.rest, k - 1
    return sum


def overlap(s, t):
    """For increasing s and t, count the numbers that appear in both.

    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8)))))
    >>> overlap(a, b)  # 3 and 7
    2
    >>> overlap(a.rest, b)  # just 7
    1
    >>> overlap(Link(0, a), Link(0, b))
    3
    """
    "*** YOUR CODE HERE ***"
    count = 0
    while s is not Link.empty and t is not Link.empty:
        if s.first == t.first:
            count += 1
        elif s.first < t.first:
            s = s.rest
        else:
            t = t.rest
    return count

def overlapRecursive(s, t):
    """For increasing s and t, count the numbers that appear in both.

    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8)))))
    >>> overlap(a, b)  # 3 and 7
    2
    >>> overlap(a.rest, b)  # just 7
    1
    >>> overlap(Link(0, a), Link(0, b))
    3
    """
    "*** YOUR CODE HERE ***"
    if s is Link.empty or t is Link.empty:
        return 0
    if s.first == t.first:
        return 1 + overlapRecursive(s.rest, t.rest)
    elif s.first < t.first:
        return overlapRecursive(s.rest, t)
    else:
        return overlapRecursive(s, t.rest)
    
def display(s, k=10):
    """Print the first k digits of infinite linked list s as a decimal.

    >>> s = Link(0, Link(8, Link(3)))
    >>> s.rest.rest.rest = s.rest.rest
    >>> display(s)
    0.8333333333...
    """
    assert s.first == 0, f'{s.first} is not 0'
    digits = f'{s.first}.'
    s = s.rest
    for _ in range(k):
        assert s.first >= 0 and s.first < 10, f'{s.first} is not a digit'
        digits += str(s.first)
        s = s.rest
    print(digits + '...')

def sequenceGenerator(s):
    while True:
        yield from s

def divide(n, d):
    """Return a linked list with a cycle containing the digits of n/d.

    >>> display(divide(5, 6))
    0.8333333333...
    >>> display(divide(2, 7))
    0.2857142857...
    >>> display(divide(1, 2500))
    0.0004000000...
    >>> display(divide(3, 11))
    0.2727272727...
    >>> display(divide(3, 99))
    0.0303030303...
    >>> display(divide(2, 31), 50)
    0.06451612903225806451612903225806451612903225806451...
    """
    assert n > 0 and n < d
    result = Link(0)  # The zero before the decimal point
    "*** YOUR CODE HERE ***"
    numer_to_sequence = {}
    tail = result 
    while True:
        q = 10 * n // d
        r = 10 * n % d # the remainder is what we will use to calculate the next digit
        tail.rest = Link(q)
        numer_to_sequence[n] = tail.rest # store that link instance so we can refer back to it
        tail = tail.rest
        n = r # if our remainder is a numerator we've encountered before
        if n in numer_to_sequence: # if we encounter the same numerator, we can just point back to that Link
            tail.rest = numer_to_sequence[n]
            break
    return result

display(divide(1, 3))

display(divide(4, 5))


def reverse(list):
    def helper(l, soFar):
        if l is Link.empty:
            return soFar
        return helper(l.rest, Link(l.first, soFar)) # put the next element before what we've done so far
    return helper(list, Link.empty)

x = Link(4, Link(3, Link(2, Link(1))))
print(x)
x = reverse(x)
print(x)


import time

def squares2(total, k):
    if total == k * k:
        yield [total]
    elif total > k * k:
        for s in squares2(total - k * k, k):
            s.append(k * k)
            yield s # we .append returns None
        yield from squares2(total, k + 1)

def squares(total, k):
    if total == k * k: # we need to return a list of lists
        return [[total]]
    elif total < k * k:
        return None # when not using generators we need to return lists nested like this
    res = squares(total - k * k, k)
    res2 = squares(total, k + 1)
    if res is not None:
        for s in res: # retrieved a list of possible solutions using k * k 
            s.append(k * k)
        if res2 is not None:
            res.extend(res2)
        return res
    if not res and res2: # res was None, res2 was fine
        return res2

size = 95

s = time.time()
print(squares(size, 2))
print("time taken directly", time.time() - s)

# s = time.time()
# list(squares(size, 1))
# print("time taken appending", time.time() - s)
s = time.time()
print(list(squares2(size, 2)))
print("time taken with generator", time.time() - s)



        