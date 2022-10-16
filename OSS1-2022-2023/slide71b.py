x = int((input("Δώσε x:")))
y = int((input("Δώσε y:")))
z = int((input("Δώσε z:")))

if x>=y and x>=z:
  print("max is:", x)
elif y>=x and y>=z:
  print("max is:", y)
elif z>=x and z>=y:
  print("max is:", z)
