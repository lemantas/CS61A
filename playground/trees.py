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
        
