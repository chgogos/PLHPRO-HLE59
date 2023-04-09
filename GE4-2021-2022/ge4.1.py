import pickle # Χρήση της βιβλιοθήκης pickle για τη σειριοποίηση του λεξικού

class Store():
    '''κλάση για ανάκτηση και αποθήκευση δεδομένων σε ένα αρχείο pickle'''
    def __init__(self, f):
        self.store = f

    def load(self):
        try:
            with open(self.store, "rb") as f:
                return pickle.load(f)
        except: # error in opening file
            return {}

    def save(self, data):
        try:
            with open(self.store, "wb") as f:
                pickle.dump(data, f)
            print('επιτυχής αποθήκευση δεδομένων')
        except Exception as e:
            print ('σφάλμα στην αποθήκευση των δεδομένων', e)

class AddressBook():
    '''κλάση για διαχείριση επαφών'''
    def __init__(self, f):
        self.store = Store(f)
        self.epafes = self.store.load()
        self.contactsManagement()
        self.store.save(self.epafes)

    def contactsManagement(self):
        ''''Απλή διαχείριση επαφών με εισαγωγή νέων επαφών και εκτύπωση επαφών.'''
        while True:
            reply = input('πατήστε + για νέα επαφή, ? για λίστα επαφών ή <enter> για έξοδο\n>>> ')
            if not reply: break
            if reply == '+':
                name = input('όνομα: ')
                phone = input('τηλέφωνο: ')
                if name and phone: self.epafes[name] = phone
                else:print('παρακαλώ δώστε στοιχεία')
            elif reply == '?':
                self.showContacts()

    def showContacts(self):
        for e in sorted(self.epafes):
            print(f'{e}: {self.epafes[e]}')

if __name__ == '__main__':
    addressbookFilename = "addressbook"
    AddressBook(addressbookFilename)
