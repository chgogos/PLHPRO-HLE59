x = int((input("Δώσε x:")))
y = int((input("Δώσε y:")))
z = int((input("Δώσε z:")))

if x > y:
    if x > z:
        print("max is:", x)
    else:
        print("max is:", z)
else:
    if y > z:
        print("max is:", y)
    else:
        print("max is:", z)
