astring=""		# αρχικοποίηση συμβολοσειράς
char_position=-1	# αρχικοποίηση χαρακτήρα αναζήτησης

# ερώτημα (α)
while (astring==""): # αμυντικός προγραμματισμός για μη κενή συμβολοσειρά
    astring=input("Παρακαλω εισάγετε μία συμβολοσειρά: ") # είσοδος 

# ερώτημα (β) 
while (char_position < 1 or char_position > len(astring)): # αμυντικός προγραμματισμός
    char_position=int(input("Παρακαλώ εισάγετε τη θέση του προς αφαίρεση χαρακτήρα: ")) # είσοδος
new_string = astring[:char_position-1] + astring[char_position:]
print("Η νέα συμβολοσειρά: {}".format(new_string)) # εκτύπωση συμβολοσειράς εξαιρουμένου του χαρακτήρα στην θέση char_position

# ερώτημα (γ)
achar=input("Παρακαλω εισάγετε έναν χαρακτήρα: ") # είσοδος χαρακτήρα
print("Ο χαρακτήρας {} εμφανίζεται {} φορές στη συμβολοσειρά: {}".format(achar, astring.count(achar),astring))
print("To ποσοστό των εμφανίσεων του χαρακτήρα {} στην αρχική συμβολοσειρά είναι {}%".format(achar, int(100*astring.count(achar)/len(astring))))
print(" ")
print("\tΟλοκληρώθηκε η εκτέλεση του προγράμματος")


