def factorial_recursive(num):
    """αναδρομικός υπολογισμός παραγοντικού"""
    if num == 0 or num == 1:
        return 1
    return num * factorial_recursive(num - 1)


def factorial_iteration(num):
    """επαναληπτικός υπολογισμός παραγοντικού"""
    if num == 0 or num == 1:
        return 1
    p = 1
    for i in range(1, num + 1):
        p *= i
    return p


print(factorial_recursive(5))
print(factorial_iteration(5))
