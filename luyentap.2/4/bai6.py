def tim_so_hoan_hao(a, b):
    for i in range(a, b + 1):
        if la_so_hoan_hao(i):
            print(i, end=" ")
    print()