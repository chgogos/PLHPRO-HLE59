# Άρθρωμα/module καλαθιού αγορών


class Market:
    '''Κλάση καταστημάτων πώλησης αγαθών (προϊόντων).'''

    def __init__(self, *product_list):
        '''Δημιουργία καταστήματος με λίστα των προϊόντων που διαθέτει.'''
        self.products = product_list

    def product_name(self, product_no):
        '''Επιστροφή του κόστους προϊόντος.'''
        return(self.products[product_no][0])

    def product_cost(self, product_no):
        '''Επιστροφή του κόστους προϊόντος.'''
        return(self.products[product_no][1])

    def show_products(self):
        '''Εμφάνιση προϊόντων καταστήματος.'''
        for i in range(len(self.products)):
            print(f"Προϊόν #{i}: {self.product_name(i)}")

    def select_product(self):
        '''Παρουσίαση προϊόντων και είσοδος επιλογής.'''
        while True:
            self.show_products()
            try:
                selected_product = int(input("Επέλεξε αριθμό προϊόντος: "))
            except ValueError:
                print("Παρακαλώ εισάγετε ακέραια τιμή")
                continue
            if selected_product in range(len(self.products)):
                return selected_product
            else:
                print("Παρακαλώ εισάγετε μία έγκυρη τιμή. ", end="")
                print(f"Η τιμή {selected_product} δεν είναι έγκυρη.")


class ShoppingCart:
    '''Κλάση καλαθιού αγορών.'''
    
    def __init__(self, market):
        '''Δημιουργία (άδειου) καλαθιού με αναφορά στο κατάστημά του.''' 
        self.market = market
        self.contents = []
        self.shopping_cart_management()

    def add_products(self):
        '''Προσθέτει προϊόντα στο καλάθι αγορών'''
        finished = False
        while not finished:
            product = self.market.select_product()
            quantity_selected = False
            while not quantity_selected:
                try:
                    quantity = int(input("Εισάγετε την επιθυμητή ποσότητα: "))
                except ValueError:
                    print("Παρακαλώ εισάγετε ακέραια τιμή")
                    continue
                if quantity > 0:
                    quantity_selected = True
                    self.contents.append((product, quantity))
                else:
                    print("Παρακαλώ εισάγετε θετική ποσότητα")
            cont = input("Επιθυμείτε να εισάγετε άλλο προϊόν (ν/ο): ")
            if cont in "oοOΟ" and len(cont)>0:
                finished = True

    def display_basket(self):
        '''Εμφανίζει το περιεχόμενο του καλαθιού αγορών'''
        total = 0
        line = 0
        print(
            "{:>3}   {:<23}   {:>3}   {:>8}   {:>6}".format(
                "AA", "ΕΙΔΟΣ", "ΤΜΧ", "ΤΙΜΗ ΤΜΧ", "ΑΞΙΑ"
            )
        )
        for p in self.contents:
            line += 1
            product_index = p[0]
            line_product_name = self.market.product_name(product_index)
            product_value = self.market.product_cost(product_index)
            quantity = p[1]
            line_value = product_value * quantity
            total += line_value
            print(
                "{:>3}   {:<23}   {:>3}   {:>8}   {:>6}".format(
                    str(line) + ".",
                    line_product_name,
                    quantity,
                    str(product_value) + "€",
                    str(line_value) + "€",
                )
            )
        print("{:>55}".format("ΣΥΝΟΛΟ: " + str(total) + "€"))
        return total

    def remove_product(self):
        '''Αφαιρεί προϊόντα από το καλάθι αγορών'''
        self.display_basket()
        selected_product = -1
        while selected_product == -1:
            try:
                selected_product = int(input("Επέλεξε γραμμή προϊόντος προς αφαίρεση: "))
            except ValueError:
                print("Παρακαλώ εισάγετε αριθμητική τιμή")
                continue
            if selected_product not in range(1, len(self.contents) + 1):
                print("Παρακαλώ εισάγετε μία έγκυρη τιμή.", end="")
                print(f"Η τιμή {selected_product} δεν είναι έγκυρη")
                selected_product = -1
        verification = input("Παρακαλώ επιβεβαιώστε την αφαίρεση (ν/ο): ")
        if verification in "νΝ":
            self.contents.pop(selected_product - 1)
            print("Το προϊόν αφαιρέθηκε επιτυχώς από το καλάθι αγορών")
        else:
            print("Το προϊόν δεν αφαιρέθηκε!")

    def buy_products(self):
        '''Επιβεβαίωση αγοράς και υπολογισμός τιμής'''
        if len(self.contents) == 0:
            print("Άδειο καλάθι")
            return
        total = self.display_basket()
        verification = input("Παρακαλώ επιβεβαιώστε την αγορά (ν/ο): ")
        if verification in "νΝ":
            is_member = input("Έχετε κάρτα μέλους (ν/ο): ")
            if is_member in "νΝ":
                discount = round(total * 0.07, 2)
                total = total - discount
                print("Έκπτωση " + str(discount) + "€")
            print("Παρακαλούμε πληρώστε " + str(total) + "€")
            self.contents.clear()
            print("Σας ευχαριστούμε για την αγορά σας!")
        else:
            print("Η αγορά ακυρώθηκε!")

    def shopping_cart_management(self):
        while True:
            print("Επιλογές")
            print("========")
            print("1. Προσθήκη προϊόντων στο καλάθι, ", end="")
            print("2. Εμφάνιση περιεχομένου καλαθιού, ", end="")
            print("3. Αφαίρεση προϊόντος, ", end="")
            print("4. Πληρωμή, ", end="")
            print("5. Αποθήκευση καλαθιού, ", end="")
            print("6. Ανάκληση καλαθιού")
            choice = input("Εισάγετε την επιλογή σας:")
            if choice == "1":
                self.add_products()
            elif choice == "2":
                self.display_basket()
            elif choice == "3":
                self.remove_product()
            elif choice == "4":
                self.buy_products()
                break
            else:
                print("Παρακαλώ εισάγετε έγκυρη επιλογή")
