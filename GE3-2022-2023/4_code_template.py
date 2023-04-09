# 
#                               --->  Fuel Pump 
#       Ignition -->  Battery --                   
#                               --->  Engine  
#
class Component:
    def __init__(self,name):
        # Αρχικοποίηση ονόματος, κατάστασης και δομής αποθήκευσης συνδεδεμένων εξαρτημάτων
        self.name = name

    
    def connect(self, other):
        # Προσθήκη εξαρτήματος στη δομή αποθήκευσης συνδεδεμένων εξαρτημάτων
        pass
    
    def start(self):
        # Αλλαγή κατάστασης, εκκίνηση συνδεδεμένων εξαρτημάτων και εκτύπωση μηνύματος έναρξης του κάθε εξαρτήματος
        pass 

    def stop(self):
        # Αναστολή λειτουργίας συνδεδεμένων εξαρτημάτων, αλλαγή κατάστασης και εκτύπωση μηνύματος αναστολής του εξαρτήματος
        pass 

    def status(self):
        # Εκτύπωση συνδεδεμένων εξαρτημάτων και κατάστασης εξαρτήματος 
        pass 

class Ignition(Component):  
    def __init__(self):
        super().__init__("Μίζα")

class Battery(Component):
    def __init__(self):
        super().__init__("Μπαταρία")

class FuelPump(Component):  
    def __init__(self):
        pass

class Engine(Component):
    def __init__(self):
        pass

class Car:
    def __init__(self):
        # Δημιουργία των εξαρτημάτων του αυτοκινήτου
        self.ignition = Ignition()


        # Σύνδεση των εξαρτημάτων μεταξύ τους
        self.ignition.connect(self.battery)

    def status(self):
        print('=========================')
        self.ignition.status()
        print('=========================')


ign = Ignition()
print(ign.name)
bat = Battery()
print(bat.name)
