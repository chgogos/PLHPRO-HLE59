a = 'Hello'


def hello(new_a):
    global a
    a = new_a
    b = 'World!'
    c = a + ' ' + b
    return c


print(hello('Demo'))
print(a)
