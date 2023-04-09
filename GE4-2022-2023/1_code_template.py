# Εφαρμογή καλαθιού αγορών που μπορεί να αποθηκευτεί σε αρχείο

# Είσοδος (import) των κλάσεων για το χειρισμό καλαθιού αγορών,
# ώστε (με χρήση κληρονομικότητας) να δημιουργήσουμε κλάση καλαθιού
# που μπορεί να αποθηκευτεί.
# Γίνεται με from για να μην χρειάζεται να χρησιμοποιούμε το όνομα
# του module.
#
# ΠΡΟΣΟΧΗ: Το αρχείο market.py πρέπει να βρίσκεται στον ίδιο φάκελο
# με το αρχείο της απάντησής σας. 
from market import *

# Χρήση της βιβλιοθήκης pickle για την αποθήκευση και ανάκληση
# των περιεχομένων του καλαθιού
import pickle 


class ShoppingCartStore():
    '''Κλάση αποθήκευσης περιεχομένων καλαθιού σε αρχείο pickle'''

    def __init__(self, filename):
        '''Αρχικοποίηση αποθήκης περιεχομένων καλαθιού.'''
        self.store = filename

    def save(self, data):
        '''Αποθήκευση σε αρχειο pickle.'''
        # Υποερώτημα α
        pass

    def load(self):
        '''Ανάκληση από σε αρχείο pickle.'''
        # Υποερώτημα β
        pass


class StorableShoppingCart(ShoppingCart):
    '''Κλάση καλαθιού αγορών που μπορεί να αποθηκευτεί.'''
    
    def __init__(self, market, filename):
        '''Δημιουργία (άδειου) καλαθιού που μπορεί να αποθηκευτεί.''' 
        # Υποερώτημα γ

        # Αρχικοποίηση των άλλων ιδιοτήτων με χρήση της γονικής __init__ 
        super().__init__(market)

    def shopping_cart_management(self):
        '''Χειρισμός λειτουργιών καλαθιού.''' 
        while True:
            print("Επιλογές")
            print("========")
            print("1. Προσθήκη προϊόντων στο καλάθι, ", end="")
            print("2. Εμφάνιση περιεχομένου καλαθιού, ", end="")
            print("3. Αφαίρεση προϊόντος, ", end="")
            print("4. Πληρωμή, ", end="")
            print("5. Αποθήκευση καλαθιού, ", end="")
            print("6. Ανάκληση καλαθιού")
            choice = input("Εισάγετε την επιλογή σας: ")
            if choice == "1":
                self.add_products()
            elif choice == "2":
                self.display_basket()
            elif choice == "3":
                self.remove_product()
            elif choice == "4":
                self.buy_products()
                break
            # Υποερώτημα δ

            else:
                print("Παρακαλώ εισάγετε έγκυρη επιλογή")


if __name__ == "__main__":
    mini_market_products = [
        ("ΓΑΛΑ 1LT", 1.5),
        ("ΓΙΑΟΥΡΤΙ ΣΤΡΑΓΓΙΣΤΟ 2%", 2.0),
        ("ΠΑΓΩΤΟ", 2.5),
        ("ΝΕΣ ΚΑΦΕ", 7.5),
        ("ΜΠΙΣΚΟΤΑ ΓΕΜΙΣΤΑ", 1.0),
        ("ΣΑΛΑΤΑ ΣΕΦ", 1.0),
        ("ΤΥΡΙ ΤΟΣΤ", 6.0),
        ("ΕΞ. ΠΑΡΘΕΝΟ ΕΛΑΙΟΛΑΔΟ", 8.0),
        ("ΚΑΦΕΣ ΦΙΛΤΡΟΥ", 7.0),
        ("ΨΩΜΙ ΤΟΣΤ", 1.5),
    ]
    mini_market = Market(*mini_market_products)
    cart_file = "mycart"
    StorableShoppingCart(mini_market, cart_file)





