print("ΠΑΙΧΝΙΔΙ: ΜΑΝΤΕΨΕ ΤΟΝ ΑΡΙΘΜΟ!")

secret = 42	# Ο ένας παίκτης αλλάζει τον μυστικό αριθμό, ο άλλος προσπαθεί να τον μαντέψει.

print("Σκέφτηκα έναν ακέραιο από 1 ως 100. Βρες ποιος είναι.")

count = 0
while True:
  guess = int(input("Μάντεψε: "))
  count = count + 1
  if guess == secret:
    print("Μπράβο! Τον βρήκες με", count, "προσπάθειες.")
    break
  elif guess < secret:
    print("Όχι, ο αριθμός μου είναι μεγαλύτερος από", guess)
  else:   # guess>secret
    print("Όχι, ο αριθμός μου είναι μικρότερος από", guess)

print("Τέλος παιχνιδιού.")
