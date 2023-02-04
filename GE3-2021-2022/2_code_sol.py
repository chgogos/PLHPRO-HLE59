# ΕΑΠ- ΘΕ ΠΛΗΠΡΟ - Γραπτή Εργασία 3 - Υπoεργασία 2

class Student():
    def __init__(self, arithmos_mitroou, name, vathmos):
        self.name = name
        self.am = str(arithmos_mitroou)
        self.vathmos = float(vathmos)
    def __str__(self):
        return f"[{self.am:5s}] {self.name:20s}    {self.vathmos:.1f}"
#--------------------------
class Control():
    theStudents = {}

    def __init__(self):
        self.run()
    
    def add_student(self):
        while True:
            st = input('δώσε στοιχεία φοιτητή ΑΜ,ΟΝΟΜΑ,ΒΑΘΜΟΣ(enter για τέλος): ')
            if not st: break
            if len(st.split(',')) != 3: continue
            am, name, grade = st.split(',')
            if not am.isdigit() or len(name)<3 : continue
            try:
                grade = float(grade)
            except: 
                print('παρακαλώ δώστε αριθμό')
                continue
            if am in Control.theStudents.keys():
                reply = input(f'ΠΡΟΣΟΧΗ: φοιτητής με αριθμό μητρώου {am} υπάρχει, να αλλάξουν τα στοιχεία του(N/O);')
                if reply.upper() in 'ΟO': continue
            Control.theStudents[am] = Student(am, name, grade)
            print(f'Προστέθηκε ένας φοιτητής, συνολικό πλήθος: {len(Control.theStudents)}')
            break       

    def delete_student(self):
        am = input('Αριθμός Μητρώου φοιτητή για διαγραφή:')
        if am not in Control.theStudents:
            print(f'Δεν βρέθηκε ο φοιτητής με αριθμ.μητρ={am}')
        else:
            del(Control.theStudents[am])
            print('Επιτυχής διαγραφή φοιτητή')

    def show_students(self):
        for am in sorted(Control.theStudents, key=int):
            print(Control.theStudents[am])

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
