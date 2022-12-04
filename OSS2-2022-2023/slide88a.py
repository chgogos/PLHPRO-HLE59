def pascal_triangle(n):
    triangle = []

    for i in range(n):
        triangle.append([1] * (i + 1))
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    for x in triangle:
        print(x)
    return triangle[-1]


pt = pascal_triangle(5)
