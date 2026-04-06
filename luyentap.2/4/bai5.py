def la_so_hoan_hao(n):
    tong = 0
    i = 1
    
    while i < n:
        if n % i == 0:
            tong = tong + i
        i = i + 1
    
    if tong == n:
        return True
    else:
        return False