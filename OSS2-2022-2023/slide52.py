A = {"a", "2", "test", "b", 23}
B = {"a", "3", "b", "E", 24}

C = A.symmetric_difference(B)
print("C: ", C, ", μέγεθος: ", len(C))
msg = "Η λέξη test δεν υπάρχει σε κανένα σύνολο"
if "test" in A:
    msg = "Η λέξη test είναι στο σύνολο Α"

if "test" in B:
    msg = "Η λέξη test είναι στο σύνολο Β"

a = 0
for x in C:
    a += 1
    print(a, " : ", x, ", type: ", type(x))

print(msg, "\nΤέλος προγράμματος")
