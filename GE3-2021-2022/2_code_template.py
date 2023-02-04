# ΕΑΠ- ΘΕ ΠΛΗΠΡΟ - Γραπτή Εργασία 3 - Υποεργασία 2

class Student():
    def __init__(self, arithmos_mitroou, name, vathmos):
        self.name = name
        self.am = str(arithmos_mitroou)
        self.vathmos = float(vathmos)
    def __str__(self):
        return f"[{self.am:5s}] {self.name:20s}    {self.vathmos:.1f}"
#--------------------------
class Control():
    theStudents = {} # μεταβλητή επιπέδου κλάσης, χρήση: Control.theStudents

    def __init__(self):
        self.run()    
    def add_student(self):
        pass # Ερώτημα (α)-συμπληρώστε τη μέθοδο προσθήκης νέου φοιτητή
    def delete_student(self):
        pass # Ερώτημα (β)-συμπληρώστε τη μέθοδο διαγραφής φοιτητή
    def show_students(self):
        pass # Ερώτημα (γ)-συμπληρώστε τη μέθοδο εμφάνισης των φοιτητών

    def run(self):
        while True:
            print('Προσθήκη φοιτητή (+), διαγραφή φοιτητή (x), εμφάνιση φοιτητών (?), <enter> για έξοδο')
            reply = input("...")
            if not reply: break
            if reply == "+":
                self.add_student()
            elif reply == "x":
                self.delete_student()
            elif reply == "?":
                self.show_students()
#--------------------------
if __name__ == "__main__":
    Control()
