def la_so_nguyen_to(n):
    if n < 2:
        return False
    
    i = 2
    while i <= n - 1:
        if n % i == 0:
            return False
        i = i + 1
    
    return True