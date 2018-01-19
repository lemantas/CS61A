# an oak or a maple - whatever, it's a tree
def tree(value, branches=[]):
    for branch in branches:
        assert is_tree(branch), "branches must be trees"
    return [value] + list(branches)
    
# selectors
def root(tree):
    return tree[0]
    
def branches(tree):
    return tree[1:]
    
# let's check if the plant is real
def is_leaf(tree):
    return not branches(tree)
    
def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

# is this possible in the physical world?    
def square_tree(t):
    if is_leaf(t):
        return tree(pow(root(t), 2))
    else:
        return tree(pow(root(t), 2), [square_tree(branch) for branch in branches(t)])

# the longest path from root to leaf        
def height(t):
    if is_leaf(t):
        return 1
    else:
        return 1 + max([height(branch) for branch in branches(t)])
        
# the number of nodes in a tree        
def tree_size(t):
    def count(t):
        if is_leaf(t):
            return 1
        else:
            return 1 + sum([count(branch) for branch in branches(t)])
    return count(t) - 1
    
# the largest number in a tree
def tree_max(t):
    def get_max(t, n):
        if root(t) > n:
            n = root(t)
        if is_leaf(t):
            return n
        else:
            return max([get_max(branch, n) for branch in branches(t)])
    return get_max(t, root(t))
 
        
""" EXTRA QUESTIONS BELOW """

# some helper funtions
def reduce(fn, s, init):
    reduced = init
    for x in s:
        reduced = fn(reduced, x)
    return reduced

def apply_to_all(fn, s):
    return [fn(x) for x in s]
    
from operator import add, mul
# I think this is not generalized enough, but let it be for now...
def eval_tree(tree):
    """Evaluates an expression tree with functions as root
    >>> eval_tree(tree(1))
    1
    >>> expr = tree(mul, [tree(2), tree(3)])
    >>> eval_tree(expr)
    6
    >>> eval_tree(tree(add, [expr, tree(4)]))
    10
    """
    if is_leaf(tree):
        return root(tree)
    else:
        fn = root(tree)
        init = 0 if fn == add else 1
        return reduce(fn, apply_to_all(eval_tree, branches(tree)), init)
    
def hailstone_tree(n, h):
    """Generates a tree of hailstone numbers that will reach N
    , with height H.
    >>> hailstone_tree(1, 0)
    [1]
    >>> hailstone_tree(1, 4)
    [1, [2, [4, [8, [16]]]]]
    >>> hailstone_tree(8, 3)
    [8, [16, [32, [64]], [5, [10]]]]
    """
    if h == 0:
        return tree(n)
    else:
        branches = [hailstone_tree(2 * n, h - 1)]
        if ((n - 1) % 3 == 0) and (n not in [1, 4]):
            branches.append(hailstone_tree((n - 1) // 3, h - 1))
        return tree(n, branches)
