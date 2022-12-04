li = [10, 5, 125, 44, 2]
num = int(input("Δώστε έναν αριθμό: "))
index = 0
msg = "O αριθμός {}, δεν υπάρχει στην λίστα.".format(num)

for x in li:
    if x == num:
        msg = "Ο αριθμός {} είναι στην θέση {} .".format(num, index)
        break
    index += 1

print(msg, "\nΤέλος προγράμματος")
