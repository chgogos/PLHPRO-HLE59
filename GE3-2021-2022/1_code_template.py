# ΕΑΠ- ΘΕ ΠΛΗΠΡΟ - Γραπτή Εργασία 3 - Υποεργασία 1

class Stack():
    def  __init__(self):
        pass # Ερώτημα (α)-να συμπληρώσετε τον κατασκευαστή της κλάσης Stack
    def  push(self,item):
        pass # Ερώτημα (β)
    def  pop(self):
        pass # Ερώτημα (γ)
    def  __str__(self):
        # Ερώτημα (δ)
        return '->\t' + "\n\t".join(reversed(self.content))

class Control():
    s = Stack()
    while True:
        r = input('+item για ώθηση, - για απώθηση, ? για παρουσίαση, x για έξοδο:')
        if r[0] == 'x': break
        if r[0] == '+' and len(r.strip()) > 1: s.push(r.strip()[1:])
        if r[0] == '-' : s.pop()
        if r[0] == '?' : print(s)
