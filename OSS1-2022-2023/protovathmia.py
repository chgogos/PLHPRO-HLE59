# Πρωτοβάθμια εξίσωση της μορφής ax+b=0
# Η λύση υπολογίζεται σε x=-b/a, εφόσον το a δεν είναι 0

# Εισαγωγή συντελεστών
a = int(input("Δώστε το a:"))
b = int(input("Δώστε το b:"))

# Έλεγχος για το a
if a!=0:
    x = -b/a
    print("x=", x)
else:
    print("Η εξίσωση είναι αδύνατη")
