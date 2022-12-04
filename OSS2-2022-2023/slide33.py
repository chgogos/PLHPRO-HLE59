li = [10, 5, 125, 44, 2]
num = int(input("Δώστε έναν αριθμό: "))
for i, x in enumerate(li):
    if x == num:
        print("Ο αριθμός {} είναι στην θέση {}.".format(num, i))
        break
    else:
        print("O αριθμός {} δεν υπάρχει στην λίστα.".format(num))
