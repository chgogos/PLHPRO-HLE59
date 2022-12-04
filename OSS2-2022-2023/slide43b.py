t = ('a', 'b', 'c', 'd', 'e')
print("T: ", t)
val = input("Δώστε μια συμβολοσειρά :")

li = list(t)
li[2] = val
t = tuple(li)

print("T: ", t)
print("T type:", type(t))
print("Τέλος προγράμματος")
