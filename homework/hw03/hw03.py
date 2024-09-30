HW_SOURCE_FILE=__file__


def num_eights(n):
    """Returns the number of times 8 appears as a digit of n.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 0: #base case
        return 0
    
    if n % 10 == 8: # increment count by 1
        return 1 + num_eights(n // 10)
    else:
        return num_eights(n // 10)

def digit_distance(n):
    """Determines the digit distance of n.

    >>> digit_distance(3)
    0
    >>> digit_distance(777) # 0 + 0
    0
    >>> digit_distance(314) # 2 + 3
    5
    >>> digit_distance(31415926535) # 2 + 3 + 3 + 4 + ... + 2
    32
    >>> digit_distance(3464660003)  # 1 + 2 + 2 + 2 + ... + 3
    16
    >>> from construct_check import check
    >>> # ban all loops
    >>> check(HW_SOURCE_FILE, 'digit_distance',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    def digit_distance_helper(rest, prevDigit):
        if rest == 0:
            return 0
        return abs(rest % 10 - prevDigit) + digit_distance_helper(rest // 10, rest % 10)

    return digit_distance_helper(n // 10, n % 10)

def interleaved_sum(n, odd_func, even_func):
    """Compute the sum odd_func(1) + even_func(2) + odd_func(3) + ..., up
    to n.

    >>> identity = lambda x: x
    >>> square = lambda x: x * x
    >>> triple = lambda x: x * 3
    >>> interleaved_sum(5, identity, square) # 1   + 2*2 + 3   + 4*4 + 5
    29
    >>> interleaved_sum(5, square, identity) # 1*1 + 2   + 3*3 + 4   + 5*5
    41
    >>> interleaved_sum(4, triple, square)   # 1*3 + 2*2 + 3*3 + 4*4
    32
    >>> interleaved_sum(4, square, triple)   # 1*1 + 2*3 + 3*3 + 4*3
    28
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'interleaved_sum', ['While', 'For', 'Mod']) # ban loops and %
    True
    >>> check(HW_SOURCE_FILE, 'interleaved_sum', ['BitAnd', 'BitOr', 'BitXor']) # ban bitwise operators, don't worry about these if you don't know what they are
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(k): # k is always odd
        if k > n:
            return 0
        elif k == n: #we need to apply the odd func one more time
            return odd_func(k)
        return odd_func(k) + even_func(k + 1) + helper(k + 2)
    return helper(1) #this is a far more elegant solution to the one below
    """def interleaved_sum_odd(n, index):
        if index > n:
            return 0
        
        return odd_func(index) + interleaved_sum_even(n, index + 1)
    
    def interleaved_sum_even(n, index):
        if index > n: 
            return 0
    
        return even_func(index) + interleaved_sum_odd(n, index + 1)
    
    return interleaved_sum_odd(n, 1)"""

def next_smaller_dollar(bill):
    """Returns the next smaller bill in order."""
    if bill == 100:
        return 50
    if bill == 50:
        return 20
    if bill == 20:
        return 10
    elif bill == 10:
        return 5
    elif bill == 5:
        return 1

def count_dollars(total):
    """Return the number of ways to make change.

    >>> count_dollars(15)  # 15 $1 bills, 10 $1 & 1 $5 bills, ... 1 $5 & 1 $10 bills
    6
    >>> count_dollars(10)  # 10 $1 bills, 5 $1 & 1 $5 bills, 2 $5 bills, 10 $1 bills
    4
    >>> count_dollars(20)  # 20 $1 bills, 15 $1 & $5 bills, ... 1 $20 bill
    10
    >>> count_dollars(45)  # How many ways to make change for 45 dollars?
    44
    >>> count_dollars(100) # How many ways to make change for 100 dollars?
    344
    >>> count_dollars(200) # How many ways to make change for 200 dollars?
    3274
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_dollars', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(amount, bill):
        if amount > total or bill == None:
            return 0
        elif amount == total:
            return 1 
        sum1 = helper(amount + bill, bill)
        sum2 = helper(amount, next_smaller_dollar(bill)) #don't add the next smallest to amount
        return sum1 + sum2
    return helper(0, 100)
    """def helper(sum_so_far, bill):
        if sum_so_far > total:
            return 0
        if sum_so_far == total: #we are guranteed to hit the total exactly so this is the only base case
            return 1

        smallerBill = next_smaller_dollar(bill)
        if sum_so_far + bill > total: #should not do arms length recursion
            return helper(sum_so_far, smallerBill) #compute the sum from going to the next smaller bill
        elif smallerBill != None: #we can continue with same bill or use a smaller bill
            return helper(sum_so_far + bill, bill) + helper(sum_so_far, smallerBill)
        else: #we are using the smallest bill
            return helper(sum_so_far + bill, bill)
    #sum up the combinations we can get starting at each bill size
    return helper(100, 100) + helper(50, 50) + helper(20, 20) + helper(10, 10) + helper(5, 5) + helper(1, 1)
    """

def next_larger_dollar(bill):
    """Returns the next larger bill in order."""
    if bill == 1:
        return 5
    elif bill == 5:
        return 10
    elif bill == 10:
        return 20
    elif bill == 20:
        return 50
    elif bill == 50:
        return 100

def count_dollars_upward(total):
    """Return the number of ways to make change using bills.

    >>> count_dollars_upward(15)  # 15 $1 bills, 10 $1 & 1 $5 bills, ... 1 $5 & 1 $10 bills
    6
    >>> count_dollars_upward(10)  # 10 $1 bills, 5 $1 & 1 $5 bills, 2 $5 bills, 10 $1 bills
    4
    >>> count_dollars_upward(20)  # 20 $1 bills, 15 $1 & $5 bills, ... 1 $20 bill
    10
    >>> count_dollars_upward(45)  # How many ways to make change for 45 dollars?
    44
    >>> count_dollars_upward(100) # How many ways to make change for 100 dollars?
    344
    >>> count_dollars_upward(200) # How many ways to make change for 200 dollars?
    3274
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_dollars_upward', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(amount, bill):
        if amount > total or bill == None:
            return 0
        elif amount == total:
            return 1
        
        sum1 = helper(amount + bill, bill)
        sum2 = helper(amount, next_larger_dollar(bill))
        return sum1 + sum2
    return helper(0, 1)


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    if n == 1:
        print_move(start, end)
        return
    move_stack(n - 1, start, 6 - start - end) #move n-1 to aux
    move_stack(1, start, end) #move last to end
    move_stack(n - 1, 6 - start - end, end) #move n-1 to end
    #1. move n-1 disks to auxiliary peg
    #2. move nth disk to end peg
    #3. move n-2 disks to start/aux peg
    #4. move n-1th disk to end
    #5. repeat steps 3 and 4, each time moving one less disk

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    #fact = lambda x: 1 if x == 1 else x * fact(x - 1)
    #return (lambda f: lambda x: lambda: f(x, x - 1)(lambda x: f(x, x - 1))) (mul)
    Y = lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v)))
    return Y(lambda f: lambda n: 1 if n == 0 else n * f(n - 1))
    #return (lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))  (lambda f: lambda n: 1 if n == 0 else n * f(n - 1))
    #return lambda x: 

"""
def streak(n): 
    #base case                      #check if last and 2nd to last digit are same
    return (n >= 0 and n <= 9) or (n % 10 == n // 10 % 10 and streak(n // 10))

def smallest_factor(n):
    if n == 1:
        return 0
    k = 2
    while n % k != 0:
        k += 1
    return k

def unique_prime_factors(n):
    k = smallest_factor(n)
    def no_k(n):
        if n == 1:
            return 0
        elif n % k != 0:
            return unique_prime_factors(n) #try it on a different k
        else: # there is no remainder
            return no_k(n / k) #keep dividing by the same number until we need a different smallest factor
        
    return 1 + no_k(n) #this is where we increment
"""