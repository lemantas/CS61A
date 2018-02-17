# linear time and linear space: Theta(n) time and Theta(n) space
def exp(b, n):
    if n == 0:
        return 1
    return b * exp(b, n-1)
    
# Theta(n) time and Theta(1) space
def exp_iter(b, n):
    result = 1
    for _ in range(n):
        result = result * b
    return result
    
# Theta(log n) time and Theta(log n) space
def square(x):
    return x * x
    
def fast_exp(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(fast_exp(b, n//2))
    else:
        return b * fast_exp(b, n-1)
