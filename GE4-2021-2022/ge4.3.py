import sqlite3  #Χρήση της βιβλιοθήκης sqlite3

def show_records(table): #Συνάρτηση προβολής των εγγραφών του πίνακα table
    sql="SELECT * from {}" #Ερώτημα (query) για την προβολή των εγγραφών ενός πίνακα  
    # Υποερώτημα α 
    try: 
        with sqlite3.connect('library.db') as conn: #Σύνδεση με τη βάση δεδομένων library
            cursor = conn.cursor()
            cursor.execute(sql.format(table)) #Εκτέλεση του ερωτήματος (query) προβολής των εγγραφών του πίνακα table
            names = [description[0] for description in cursor.description] 
            print(names)  #Προβολή των ονομασιών των πεδίων του πίνακα table
            for row in cursor: 
                print(row) #Προβολή των εγγραφών του πίνακα table
            print('\n')
    except sqlite3.Error as err:  
        print ("¨Λάθος:", err) #Προβολή μηνύματος λάθους 
        return False

def insert_student(name,surname): #Συνάρτηση εισαγωγής μαθητή
    sql="INSERT INTO students(name,surname) VALUES (?,?)" #Ερώτημα (query) για την εισαγωγή του ονόματος (name) και επώνυμου (surname) του νέου μαθητή στον πίνακα students
    # Υποερώτημα β 
    try:
        with sqlite3.connect('library.db') as conn:  #Σύνδεση με τη βάση δεδομένων library
            cursor=conn.cursor()
            cursor.execute(sql,(name,surname)) #Εκτέλεση του ερωτήματος (query) για την εισαγωγή του ονόματος και του επώνυμου του νέου μαθητή στον πίνακα students
            conn.commit() #Αποθήκευση των αλλαγών στη βάση δεδομένων library
    except sqlite3.Error as err:
        print ("Λάθος:", err) #Προβολή μηνύματος λάθους 
        return False 

def delete_student(code): #Συνάρτηση διαγραφής μαθητή
    sql="DELETE FROM students WHERE id==(?)" #Ερώτημα (query) για τη διαγραφή του μαθητή βάσει του κωδικού του(id) από τον πίνακα students
    # Υποερώτημα γ 
    try:
        with sqlite3.connect('library.db') as conn:  #Σύνδεση με τη βάση δεδομένων library
            cursor=conn.cursor()
            cursor.execute(sql,(code,)) #Εκτέλεση του ερωτήματος (query) για τη διαγραφή του μαθητή από τον πίνακα students
            conn.commit() #Αποθήκευση των αλλαγών στη βάση δεδομένων library
    except sqlite3.Error as err:
        print ("Λάθος:", err) #Προβολή μηνύματος λάθους 
        return False

# Κυρίως πρόγραμμα

#Συμβολοσειρά με τις επιλογές του μενού
library_menu='''Επιλογές συστήματος:  
1) Προβολή μαθητών
2) Προβολή βιβλίων
3) Προβολή δανεισμών 
4) Καταχώρηση μαθητή
5) Διαγραφή μαθητή
6) Έξοδος
Η επιλογή σας: '''

# Κεντρικό μενού της εφαρμογής 
while True:
    entry=input(library_menu) #Εισαγωγή επιλογής μενού
    if entry =='1':
        show_records('students') #Χρήση της συνάρτησης show_records για τον πίνακα students
    elif entry == '2':
        show_records('books')  #Χρήση της συνάρτησης show_records για τον πίνακα books      
    elif entry == '3':
        show_records('lending') #Χρήση της συνάρτησης show_records για τον πίνακα lending     
    elif entry == '4':
        on=input("Καταχώρησε το όνομα του μαθητή: \n")
        ep=input("Καταχώρησε το επώνυμο του μαθητή: \n")
        insert_student(on,ep) #Χρήση της συνάρτησης insert_student
    elif entry == '5':
        student_code=input("Καταχώρησε τον κωδικό του μαθητή προς διαγραφή: \n")
        delete_student(student_code) #Χρήση της συνάρτησης delete_student
    elif entry=='6':
        break
    else: 
      print ("Λανθασμένη επιλογή. Παρακαλώ επιλέξετε 1 έως 6 \n" ) #Μήνυμα λάθους σε περίπτωση λανθασμένης επιλογής menu
