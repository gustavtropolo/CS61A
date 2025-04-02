# practice with generators
def generatePartitions(n, m):
    if n == m:
        yield [m] # this generates one value
    if n > 0 and m > 0:
        for sol in generatePartitions(n - m, m):
            yield sol + [m] # this can yield multiple solutions if the next call genPart has tree rec
        yield from generatePartitions(n, m - 1) #next, solutions with decremented m


#print(list(generatePartitions(4, 2)))

def partitions(n, m):
    if n == 0:
        return [[]]
    elif n < 0 or m == 0:
        return [] #not iterable
    solutions = [sol + [m] for sol in partitions(n - m, m)]
    solutions.extend(partitions(n, m - 1))
    return solutions
#print(partitions(6, 4))


def gen_fib():
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n

#next(filter(lambda n: n > 2024, gen_fib()))

def differences(t):
    """Yield the differences between adjacent values from iterator t.

    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    "*** YOUR CODE HERE ***"
    prev = None
    for item in t:
        if prev != None:
            yield item - prev
        prev = item


def partition_gen(n, m):
    """Yield the partitions of n using parts up to size m.

    >>> for partition in sorted(partition_gen(6, 4)):
    ...     print(partition)
    1 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 3
    1 + 1 + 2 + 2
    1 + 1 + 4
    1 + 2 + 3
    2 + 2 + 2
    2 + 4
    3 + 3
    """
    assert n > 0 and m > 0
    if n == m:
        yield str(m)
    if n - m > 0:
        "*** YOUR CODE HERE ***"
        for sol in partition_gen(n - m, m):
            yield sol + ' + ' + str(m) #larger num first
    if m > 1:
        "*** YOUR CODE HERE ***"
        yield from partition_gen(n, m - 1)

for partition in sorted(partition_gen(6, 4)):
    print(partition)