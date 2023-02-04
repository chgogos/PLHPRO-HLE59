
class BookStore:

    def __init__(self):
        pass # Αρχικοποίηση λίστας για την αποθήκευση των βιβλίων 

    def addBook(self, *args):
        pass # Προσθήκη νέου βιβλίου

    def searchBooksByAuthor(self, author=None):
        pass # Αναζήτηση βιβλίων με όνομα και επώνυμο του συγγραφέα
    
    def deleteBookWithISBN(self, isbn=None):
        pass # Διαγραφή βιβλίου με βάση το ISBN
    
    def __repr__(self):
        pass # Εκτύπωση συνόλικού πλήθους βιβλίων και λίστα βιβλίων με όλα τα στοιχεία τους 


class Book:
    def __init__(self, title, author, year, price, isbn):
        pass # Αρχικοποίηση βιβλίου
       
    def __repr__(self):
        pass # Εκτύπωση βιβλίου με όλα τα στοιχεία του


if __name__=="__main__":
    bs = BookStore()
    print("\n0) Καταχώρηση Βιβλίων\n=====================")
    bs.addBook("Python Crash Course", "Eric Matthews", 2016, 27.95, "1593279280")
    bs.addBook("Learning Python ", "Mark Lutz", 2021, 40.29, "1449355730")
    bs.addBook("Head First Python", "Paul Barry", 2017, 36.25, "7519813630")
    bs.addBook("Introduction to Machine Learning with Python", "Andreas C. Mulle", 2020, 31.99, "1449369413")
    bs.addBook("Python for Data Analysis","Wes McKinney", 2022, 38.38, "1098104032")
    bs.addBook("Deep Learning with Python", "Francois Chollet", 2017, 30.20, "1617284433")

    print("\n1) Αναζήτηση βιβλίων με το όνομα και επώνυμο συγγραφέα\n======================================================")
  
    bk = bs.searchBooksByAuthor()
    if bk:
        print("Τα βιβλία που βρέθηκαν είναι:")
        for b in bk:
            print("\t",b)
    else: print("** Δεν υπάρχουν βιβλία με αυτόν τον συγγραφέα **")

    print("\n2) Διαγραφή βιβλίου με βάση το ISBN\n===================================")
    bs.deleteBookWithISBN()

    print("\n3) Εκτύπωση όλων των διαθέσιμων βιβλίων με όλη την σχετική πληροφορία\n=====================================================================")
    print(bs)
 

