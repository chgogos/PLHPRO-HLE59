li = [10, 5, 125, 44, 2]
num = int(input("Δώστε έναν αριθμό: "))
if num not in li:
    print("O αριθμός", num, "δεν υπάρχει στην λίστα.")
else:
    print("Ο αριθμός", num, "είναι στην θέση", li.index(num))
print("Τέλος προγράμματος")
