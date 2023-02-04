# ΕΑΠ- ΘΕ ΠΛΗΠΡΟ - Γραπτή Εργασία 3 - Υπoεργασία 1

class Stack():
    def __init__(self):
        self.content = []
    def push(self, item):
        self.content.append(item)
    def pop(self):
        if self.content:
            item = self.content.pop()
            #print("η απώθηση αφαίρεσε το "+item)
            return item
        else:
            return False
    def len(self):
        return len(self.content)
    def __str__(self):
        return '->\t' + "\n\t".join(reversed(self.content))

class Control():
    s = Stack()
    while True:
        r = input('+item για ώθηση, - για απώθηση, ? για παρουσίαση, x για έξοδο:')
        if r[0] == 'x': break
        if r[0] == '+' and len(r.strip()) > 1: s.push(r.strip()[1:])
        if r[0] == '-' : s.pop()
        if r[0] == '?' : print(s)



