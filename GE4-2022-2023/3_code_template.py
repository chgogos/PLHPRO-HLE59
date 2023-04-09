import sqlite3

# Συνάρτηση προβολής των εγγραφών του πίνακα table
def show_records(table):
    '''Η συνάρτηση αυτή καλείται όταν θέλουμε να δείξουμε τις εγγραφές ενός πίνακα στη Β.Δ.'''
    sql = "SELECT * FROM {}"
    # Υποερώτημα α
    

# Συνάρτηση καταχώρησης ενός πελάτη
def register_customer(name, surname,email):
    '''Η συνάρτηση αυτή καλείται όταν θέλουμε να εισάγουμε νέα εγγραφή σε πίνακα της Β.Δ.'''
    sql = "INSERT INTO Customers (name, surname,email) VALUES (?,?,?)"
    # Υποερώτημα β
    

# Συνάρτηση για τη διαγραφή ενός πελάτη
def delete_customer(code):
    '''Η συνάρτηση αυτή καλείται όταν θέλουμε να διαγράψουμε μία εγγραφή από πίνακα της Β.Δ.'''
    sql = "DELETE FROM Customers WHERE id == (?)" 
    # Υποερώτημα γ
    
    
# Συνάρτηση η οποία καταμετρά το πλήθος των εγγραφών ενός πίνακα
def hasRows(table):
    '''Η συνάρτηση αυτή καλείται όταν θέλουμε να δούμε όλες τις εγγραφές ενός πίνακα της Β.Δ.'''
    sql = "SELECT * FROM {}"
    try:
        with sqlite3.connect('supermarket.db') as conn: #Σύνδεση με τη Β.Δ. supermarket
            cursor = conn.cursor()
            cursor.execute(sql.format(table))#Εκτέλεση του ερωτήματος (query) 
            results = cursor.fetchall()
            return results
    except sqlite3.Error as err:
            print("Error: ",err) #Προβολή μηνύματος σφάλματος
            return False


# Κυρίως Πρόγραμμα
# Συμβολοσειρά με τις επιλογές του menu της εφαρμογής
supermarket_menu = '''Επιλογές συστήματος:
1. Προβολή Πελατών
2. Προβολή Προϊόντων
3. Προβολή Αγορών
4. Καταχώρηση Πελάτη
5. Διαγραφή Πελάτη
6. Έξοδος
Δώστε την επιλογή σας: '''

# Υλοποίηση ενεργειών του menu της εφαρμογής
while True:
    choice = input(supermarket_menu)
    if choice == '1':
        # Προβολή των πελατών
         
    elif choice == '2':
        # Προβολή των προϊόντων
         
    elif choice == '3':
        # Προβολή των αγορών
         
    elif choice == '4':
        # Καταχώρηση νέου πελάτη
         
    elif choice == '5':
        # Διαγραφή πελάτη βάση του id του, κατόπιν ελέγχου, εάν υπάρχουν
        # εγγραφές εντός του πίνακα
        
    elif choice == '6':
        print("Τέλος Προγράμματος!")
        break
    else:
        # Μήνυμα λάθους σε περίπτω λανθασμένης επιλογή
        print("Λάθος επιλογή. Παρακαλώ επιλέξτε από 1 έως 6 \n") 

