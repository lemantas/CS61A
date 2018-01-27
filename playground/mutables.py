def square_elements(lst):
    """Squares every element in lst.
    >>> lst = [1, 2, 3]
    >>> square_elements(lst)
    >>> lst
    [1, 4, 9]
    """
    for i in range(len(lst)):
        lst[i] = lst[i] ** 2
        
def reverse_list(lst):
    """Reverses lst in-place (mutating the original list).
    >>> lst = [1, 2, 3, 4]
    >>> reverse_list(lst)
    >>> lst
    [4, 3, 2, 1]
    >>> pi = [3, 1, 4, 1, 5]
    >>> reverse_list(pi)
    >>> pi
    [5, 1, 4, 1, 3]
    """
    i, k = 0, len(lst)-1
    while i != k and i < k:
        lst[i], lst[k] = lst[k], lst[i]
        i += 1
        k -= 1
        
def add_this_many(x, y, lst):
    """Adds y to the end of lst the number of times x occurs.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    """
    temp = list(lst)
    for value in temp:
        if value == x:
            lst.append(y)
            
def remove_all(el, lst):
    """Removes all instances of el from lst.
    >>> x = [3, 1, 2, 1, 5, 1, 1, 7]
    >>> remove_all(1, x)
    >>> x
    [3, 2, 5, 7]
    """
    temp = lst[:]
    for i in temp:
        if i == el:
            lst.remove(i)
            
def replace_all(d, x, y):
    """
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')
    >>> d
    {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    
    Dah, doctests do not make sense with dictionaries...
    """
    for key in d.keys():
        if d[key] == x:
            d[key] = y
            
def replace_all_deep(d, x, y):
    """
    >>> d = {1: {2: 3, 3: 4}, 2: {4: 4, 5: 3}}
    >>> replace_all_deep(d, 3, 1)
    >>> d
    {1: {2: 1, 3: 4}, 2: {4: 4, 5: 1}}
    """
    for key in d.keys():
        if type(d[key]) == dict:
            replace_all_deep(d[key], x, y)
        else:
            if d[key] == x:
                d[key] = y
         
def remove_all(d, x):
    """
    >>> d = {1:2, 2:3, 3:2, 4:3}
    >>> remove_all(d, 2)
    >>> d
    {2: 3, 4: 3}
    """
    temp = dict(d)
    for key in temp.keys():
        if temp[key] == x:
            del d[key]
    del temp
