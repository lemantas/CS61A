class Tree:
    def __init__(self, entry, branches=[]):
        self.entry = entry
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches
        
    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.entry, branches_str)

    def is_leaf(self):
        return not self.branches
        
def square(x):
    return x*x

def square_tree(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5)])
    >>> square_tree(t)
    >>> t
    Tree(1, [Tree(4, [Tree(9), Tree(16)]), Tree(25)])
    """
    t.entry = square(t.entry)
    for branch in t.branches:
        square_tree(branch)
        
def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t # Assuming __repr__ is defined
    Tree(2, [Tree(2, [Tree(4)]), Tree(4), Tree(6)])
    """
    if t.entry % 2 != 0:
        t.entry += 1
    if t.branches:
        for branch in t.branches:
            make_even(branch)
        
def even(n):
    if n % 2 != 0:
        return n + 1
    else:
        return n
            
def birth_even(t):
    if t.is_leaf():
        return Tree(even(t.entry))
    else:
        branches = [birth_even(branch) for branch in t.branches]
        return Tree(even(t.entry), branches)
        
def average(t):
    vals = []
    def helper(t):
        if t.is_leaf():
            return vals.append(t.entry)
        else:
            vals.append(t.entry)
            for branch in t.branches:
                helper(branch)
    helper(t)
    return sum(vals) / len(vals)
    
def find_path(t, entry):
    """
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1)])
    >>> find_path(tree_ex, 5)
    [2, 7, 6, 5]
    """
    if t.entry == entry:
        return [t.entry]
    else:
        branches = [find_path(branch, entry) for branch in t.branches]
        for branch in branches:
            if branch:
                return [t.entry] + branch
        return False
        
class BinaryTree(Tree):
    empty = Tree(None)
    empty.is_empty = True
    
    def __init__(self, entry, left=empty, right=empty):
        for branch in (left, right):
            assert isinstance(branch, BinaryTree) or branch.is_empty
        Tree.__init__(self, entry, (left, right))
        self.is_empty = False
        
    @property
    def left(self):
        return self.branches[0]
    
    @property
    def right(self):
        return self.branches[1]
        
def height(t):
    """Returns the height of the Tree t.
    >>> t = BinaryTree(5, BinaryTree(1, BinaryTree(4, BinaryTree(999)), BinaryTree(1)), BinaryTree(2))
    >>> height(t)
    4
    """
    if t.is_empty:
        return 0
    else:
        left = height(t.left)
        right = height(t.right)
        
        return 1 + max([left, right])
