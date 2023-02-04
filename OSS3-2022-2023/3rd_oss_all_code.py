# -*- coding: utf-8 -*-
"""3rd_OSS_all_code.ipynb



# Slide 7 - Διαδικαστικός προγραμματισμός
"""
a = 10
b = 20
c = a + b
print ('1η Πρόσθεση: ', c)
d = 15
e = c + d
print ('2η Πρόσθεση : ', e)

car1_id = 1
car1_style = 'Οικογενειακό' 
car1_color = 'Πράσινο'
print(car1_id, car1_style, car1_color)

car2_id = 2
car2_style = 'Σπορ' 
car2_color = 'Κόκκινο'
print(car2_id, car2_style, car2_color)

car3_id = 3
car3_style = 'Νεανικό' 
car3_color = 'Μπλε'
print(car3_id, car3_style, car3_color)


"""# Slide 8 - Συναρτησιακός προγραμματισμός"""
def add(x,y):
    res = x + y 
    return res 

c = add(10, 20)
print ('1η Πρόσθεση: ', c)

e = add(c, 15)
print ('2η Πρόσθεση: ', e)

def car(id, st, clr):
  res = str(id) +' '+ st +' '+ clr
  return res

print(car(1, 'Οικογενειακό','Πράσινο'))
print(car(2, 'Σπορ','Κόκκινο'))
print(car(3, 'Νεανικό','Μπλε'))



"""# Slide 9 - Αντικειμενοστρεφής προγραμματισμός"""
class Mathimatika:
  def add(self, a, b):
    s = a + b
    return s

obj = Mathimatika()
c = obj.add(10, 20)

print ('1η Πρόσθεση: ', c)

e = obj.add(c, 15)
print ('1η Πρόσθεση: ', e)

class Car:
    def __init__(self, id, st, clr):
        self.id = id
        self.color = clr
        self.style = st

c1 = Car(1,'Οικογενειακό', 'Πράσινο')
print(c1.id, c1.style, c1.color)

c2 = Car(2,'Σπορ', 'Κόκκινο')
print(c2.id, c2.style, c2.color)

c3 = Car(2,'Νεανικό', 'Μπλε')
print(c3.id, c3.style, c3.color)



"""#Slide 15 - Δημιουργία κλάσης και αντικειμένου"""
class Car():
  '''This is car representation Class'''
  pass

c1 = Car()

c1.id = 1
c1.color = 'Πράσινο'
c1.style = 'Οικογενειακό'

print(c1.id, c1.style, c1.color)



"""# Slide 16 - Python και αντικείμενα"""
a = 10
print(type(a))

b = 10.5
print(type(b))

c = "Python"
print(type(c))

d = [10,'obj',10.5]
print(type(d))



"""#Slide 18 - Μέθοδοι αντικειμένων"""
class Car():

  def get_gen_info(self):
    return 'This is Car Class'



"""#Slide 19 - Μέθοδοι αντικειμένων"""
class Car():

  def get_gen_info(self):
    return 'This is Car Class'

  def get_obj_info(self):
    return str(self.id)+' - '+str(self.color)+' - '+str(self.style)

  def prepare_txt(self, x, y):
    res = str(x).upper()+' - '+str(y).upper()
    return res

c1 = Car()
c1.id = 1
c1.color = 'Πράσινο'
c1.style = 'Οικογενειακό'
print(c1.get_gen_info())

print(c1.get_obj_info())

print(c1.prepare_txt(c1.id, c1.color))



"""#Slide 21 - Μέθοδοι – Αλλαγή τιμής ιδιότητας αντικειμένου"""
class Car:

  def __init__(self, id, st, clr):
    self.id = id
    self.color = clr
    self.style = st

  def get_color(self):
    return self.color
    
  def change_color(self, new_color):
    self.color = new_color


c1 = Car(1,'Οικογενειακό', 'Πράσινο')
print(c1.id, c1.style, c1.color)

print('Χρώμα: ',c1.get_color())

c1.change_color('Μαύρο')
print('Νέο χρώμα: ',c1.get_color())



"""#Slide 22 - Μεταβλητή self μέσα στην κλάση"""
class Car:
  
  def __init__(self, id, st, clr):
    self.id = id
    self.color = clr
    self.style = st


c1 = Car(1,'Οικογενειακό', 'Πράσινο')
print(c1.id, c1.style, c1.color)



"""#Slide 23 - Μεταβλητές και ιδιότητες στις κλάσεις"""
class Car:

  counter = 0 #Μεταβλητή κλάσης

  def __init__(self, id, st, clr):
    self.id = id #Ιδιότητα στιγμιότυπου
    self.color = clr #Ιδιότητα στιγμιότυπου
    self.style = st #Ιδιότητα στιγμιότυπου
    Car.counter += 1 #Ιδιότητα κλάσης

  def get_color(self):
    return self.color
  
  def change_color(self, new_color):
    self.color = new_color

c1 = Car(1,'Οικογενειακό', 'Πράσινο')
print(c1.id, c1.style, c1.color)

c2 = Car(2,'Σπορ', 'Κόκκινο')
print(c2.id, c2.style, c2.color)

c3 = Car(3,'Νεανικό', 'Μπλε')
print(c3.id, c3.style, c3.color)

print('Αριθμός αυτοκινήτων:', Car.counter)



"""#Slide 26 - Αρχικοποίηση αντικειμένου"""
class Car:
  '''This car representation Class'''

  def __init__(self, id, st, clr):
    self.id = id
    self.color = clr
    self.style = st

c1 = Car(1,'Οικογενειακό', 'Πράσινο')

print(c1.id, c1.style, c1.color)



"""# Slide 27 - Δημιουργία πολλαπλών αντικειμένων με αρχικοποίηση"""
class Car:
  def __init__(self, id, st, clr):
    self.id = id
    self.color = clr
    self.style = st

  def get_obj_info(self):
    return str(self.id)+' - '+str(self.color)+' - '+str(self.style)

c1 = Car(1,'Οικογενειακό', 'Πράσινο')
print(c1.get_obj_info())

c2 = Car(2,'Σπορ', 'Κόκκινο')
print(c2.get_obj_info())

c3 = Car(2,'Νεανικό', 'Μπλε')
print(c3.get_obj_info())



"""#Slide 28 - Εκτύπωση αντικειμένων"""
class Car:
  def __init__(self, id, st, clr):
    self.id = id
    self.color = clr
    self.style = st
c1 = Car(1,'Οικογενειακό', 'Πράσινο')

print(Car)

print(c1)

print(c1.color)



"""#Slide 29 - Καταστροφή αντικειμένου"""
class Car:
  def __init__(self, id, st, clr):
    self.id = id
    self.color = clr
    self.style = st

  def __str__(self):
    return self.color+' '+self.style

  def __del__(self):
    print('Car {} destroyed'.format(self.id))

c1 = Car(1,'Οικογενειακό', 'Πράσινο')

print(c1)

del c1

print(c1)



"""#Slide 31 - Ισότητα αντικειμένων"""
class Car:
  def __init__(self, id, st, clr):
    self.id = id
    self.color = clr
    self.style = st
c1 = Car(1,'Οικογενειακό', 'Πράσινο')
c2 = Car(1,'Οικογενειακό', 'Πράσινο')
print(c1 == c2)

print('c1: '+str(id(c1))+' - c2: '+str(id(c2)))

c3 = c1
print(c1 == c3)

print('c1: '+str(id(c1))+' - c3: '+str(id(c3)))

c1.color = 'Κόκκινο'
print('c1 color: '+c1.color)

print('c3 color: '+c3.color)




"""#Slide 32 - Αντιγραφή αντικειμένου"""
import copy

c4 = copy.copy(c1)

print('c1: '+str(id(c1))+' - c4: '+str(id(c4)))

c1.color = 'Μαύρο'
print('c1 color: '+c1.color)

print('c4 color: '+c4.color)



"""#Slide 37 - Κληρονομικότητα"""
class Vehicle():
  def description(self):
    print("I'm a Vehicle!")

class Car(Vehicle):
  def __init__(self, id, st, clr):
    self.id = id
    self.color = clr
    self.style = st

v1 = Vehicle()
print(v1.description())

c1 = Car(1,'Οικογενειακό', 'Πράσινο')
print(c1.description())



"""#Slide 38 - Κληρονομικότητα - Override a Method"""
class Vehicle():
  def description(self):
    print("I'm a Vehicle!")

class Car(Vehicle):
  def __init__(self, id, st, clr):
    self.id = id
    self.color = clr
    self.style = st

  def description(self):
     print("I'm a Car")
v1 = Vehicle()
print(v1.description())

c1 = Car(1,'Οικογενειακό', 'Πράσινο')
print(c1.description())



"""#Slide 39 - Κληρονομικότητα – Συνάρτηση *super()*"""
class Vehicle():
  def __init__(self, clr):
    self.color = clr
  def description(self):
    print("I'm a", self.color, "Vehicle")

class Car(Vehicle):
  def __init__(self, clr, st):
    super().__init__(clr)
    self.style = st
  def description(self):
    print("I'm a", self.color, self.style)

v1 = Vehicle('Κόκκινο')
c1 = Car('Μαύρο', 'Σπορ')

v1.description()
c1.description()
v1.description()



"""#Slide 41 - Class Card()"""
class Card():
    def __init__(self, val, sym):
        self.value = val
        self.symbol = sym
        if self.symbol in "sc": self.color = 'Black'
        else: self.color = 'Red'
        if self.value in "JQK": self.fig = True
        else: self.fig = False
    
    def __repr__(self):
        return self.value+self.symbol
    def detailed_info(self):
        print(f"Αξία={self.value} Σύμβολο={self.symbol}")
        print(f"Χρώμα={self.color} Φιγούρα={self.fig}")


c = Card('K','d')
print(c)

c.detailed_info()



"""#Slide 42 - Class Deck()"""
import random

class Deck():
    values = "A23456789TJQK" # Όλες οι αξίες
    symbols = "shcd" # Όλα τα σύμβολα  
    def __init__(self): 
        self.content = []
        for s in Deck.symbols:
            for v in Deck.values: 
                c = Card(v, s)
                self.content.append(c)
    def __repr__(self):
        return str(self.content)
    def shuffle(self):
        random.shuffle(self.content)

d = Deck()
print(d)

d.shuffle()
print(d)



"""#Slide 43 - Class Pack"""
class Pack(Deck):
    def __init__(self, number_of_decks = 2):
        d = Deck()
        self.content = d.content*number_of_decks

p = Pack()
print(p)

p.shuffle()
print(p)