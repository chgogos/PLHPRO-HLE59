import turtle as tr

class Pen(tr.Turtle):
    # κλάση πέννα
    def __init__(self):
        tr.Turtle.__init__(self, "turtle")
        self.speed("fastest")
        self.ondrag(self.draw)
        self.traces = []
        # συμπληρώσετε ένα ή περισσότερα αντικείμενα τύπου Tracer (ιχνηλάτες) στη γραφίδα Pen
        # ...
        # ...

        
    def draw(self, x,y):
        self.ondrag(None)
        self.goto(x,y)
        # προσθέστε εδώ κώδικα, ώστε η κίνηση της γραφίδας από τον χρήστη, να κινεί και τους ιχνηλάτες 
        # ...
        # ...
        self.ondrag(self.draw)
        
class Tracer(tr.Turtle):
    # κλάση ιχνηλάτης
    def __init__(self, dx, dy, a=0, b=0, width=1, color='red'):
       tr.Turtle.__init__(self)
       self.hideturtle()
       self.color(color)
       self.width(width)
       self.a = a
       self.b = b
       self.dx = dx
       self.dy = dy
    def moveto(self, x,y):
        self.goto(x * self.dx + self.a, y * self.dy + self.b)

p = Pen()
tr.mainloop()
