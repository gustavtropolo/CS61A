def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

##########################################
print(tree(5, [tree(1), tree(2)])) # -> [5, [1], [2]]
print(is_tree([5, []]))

t2 = tree(5, [tree(6), tree(7)]) # -> [5, [6], [7]]
t1 = tree(3, [tree(4), t2])
# max([t1, t2], key=label) -> t2
# branches(t2) -> [[6], [7]]
# min([[6], [7]], key = label) -> [6]
# label([6]) -> 6
result = label(min(branches(max([t1, t2], key=label)), key=label))

class Path:

    def has_path(self, t, p):
        """Return whether tree t has a path from the root with labels p.

        >>> t2 = tree(5, [tree(6), tree(7)])
        >>> t1 = tree(3, [tree(4), t2])
        >>> has_path(t1, [5, 6])        # This path is not from the root of t1
        False
        >>> has_path(t2, [5, 6])        # This path is from the root of t2
        True
        >>> has_path(t1, [3, 5])        # This path does not go to a leaf, but that's ok
        True
        >>> has_path(t1, [3, 5, 6])     # This path goes to a leaf
        True
        >>> has_path(t1, [3, 4, 5, 6])  # There is no path with these labels
        False
        """
        if p == [label(t)]:  # when len(p) is 1 #since p is a list
            return True
        elif label(t) != p[0]: # [p[0]] since label(t)
            return False
        else:
            "*** YOUR CODE HERE ***"
            for b in branches(t):
                if self.has_path(b, p[1:]):
                    return True
            return False
        
    def find_path(self, t, x):
        """
        >>> t2 = tree(5, [tree(6), tree(7)])
        >>> t1 = tree(3, [tree(4), t2])
        >>> find_path(t1, 5)
        [3, 5]
        >>> find_path(t1, 4)
        [3, 4]
        >>> find_path(t1, 6)
        [3, 5, 6]
        >>> find_path(t2, 6)
        [5, 6]
        >>> print(find_path(t1, 2))
        None
        """
        if label(t) == x:
            return [label(t)]
        for b in branches(t):
            path = self.find_path(self, b, x)
            #path = [self.find_path(self, b, x) for b in branches(t) if self.find_path(self, b, x) != None]
            if path:
                return [label(t)] + path
        return None   
t2 = tree(5, [tree(6), tree(7)])
t1 = tree(3, [tree(4), t2])
print(Path.find_path(Path, t1, 5))
# [3, 5]
    

def make_path(t, p):
    assert p[0] == label(t), 'Impossible'
    if len(p) == 1:
        return t
    new_branches = []
    found_p1 = False
    for b in branches(t):
        if label(b) == p[1]:
            new_branches.append(make_path(b, p[1:])) #we will use this to create our path
            found_p1 = True
        else:
            new_branches.append(b) #the branch is not the path, include it as normal
    if not found_p1: #need to create a whole new path
        new_branches.append(make_path(tree(p[1]), p[1:])) #p[1] is the next element we need to include
    return tree(label(t), new_branches)
t1 = tree(3, [tree(4), tree(5, [tree(6), tree(7)])])
print(make_path(t1, [3, 8, 9, 1]))

def sums_new(n, m):
    res = []
    for k in range(1, min(n, m + 1)):
        for rest in sums_new(n - k, m):
            if rest[0] != k:
                res.append([k] + rest)
        
    if n <= m:
        res.append([n]) #last val
    return res

def sums_new2(n, m):
    res = []
    if n == 0:
        return [[]]
    for k in range(1, min(n + 1, m + 1)):
        for rest in sums_new2(n - k, m):
            if rest == [] or rest[0] != k:
                res.append([k] + rest)
    return res
print()
print(sums_new(7, 15))
print()
print(sums_new2(7, 15))