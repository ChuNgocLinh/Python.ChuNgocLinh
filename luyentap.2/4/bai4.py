def tim_so_nguyen_to(a, b):
    for i in range(a, b + 1):
        if la_so_nguyen_to(i):
            print(i, end=" ")
    print()