products = [("ΓΑΛΑ 1LT",1.5), ("ΓΙΑΟΥΡΤΙ ΣΤΡΑΓΓΙΣΤΟ 2%",2.0), ("ΠΑΓΩΤΟ", 2.5), ("ΝΕΣ ΚΑΦΕ", 7.5), ("ΜΠΙΣΚΟΤΑ ΓΕΜΙΣΤΑ", 1.0),
            ("ΣΑΛΑΤΑ ΣΕΦ", 1.0), ("ΤΥΡΙ ΤΟΣΤ", 6.0), ("ΕΞ. ΠΑΡΘΕΝΟ ΕΛΑΙΟΛΑΔΟ", 8.0), ("ΚΑΦΕΣ ΦΙΛΤΡΟΥ", 7.0), ("ΨΩΜΙ ΤΟΣΤ", 1.5)]

def add_products():
    pass

def display_basket():
    pass

def remove_product():
    pass

def buy_products():
    pass

if __name__ == "__main__":
    while True:
        print("Επιλογές")
        print("========")
        print("1. Προσθήκη προϊόντων στο καλάθι, 2. Εμφάνιση περιεχομένου καλαθιού, 3. Αφαίρεση προϊόντος, 4. Πληρωμή")
        choice = input("Εισάγετε την επιλογή σας:")
        if choice == "1":
            add_products()
        elif choice == "2":
            display_basket()
        elif choice == "3":
             remove_product()
        elif choice == "4":
            buy_products()
            break
        else:
            print("Παρακαλώ εισάγετε έγκυρη επιλογή")
