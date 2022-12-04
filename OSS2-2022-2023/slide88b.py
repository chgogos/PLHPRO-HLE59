def pascal_triangle(n):
    if n < 2:
        return [1]
    L = pascal_triangle(n - 1)
    print(L)
    M = []
    for i in range(n - 2):
        M.append(L[i] + L[i + 1])
    return [1] + M + [1]


pt = pascal_triangle(6)
