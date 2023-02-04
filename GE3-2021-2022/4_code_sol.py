# ΕΑΠ- ΘΕ ΠΛΗΠΡΟ - Γραπτή Εργασία 3 - Υπoεργασία 4

class Package():
    def __init__(self, description, destination):
        self.description = description
        self.destination = destination
    def cost(self):
        if self.destination == 'Αθήνα':  return 1
        elif self.destination == 'Θεσσαλονίκη': return 2
        else: return 0
    def __str__(self):
        return f"{self.description}: Προορισμός: {self.destination}, "

class Parcel(Package):
    def __init__(self, description, destination, weight):
        Package.__init__(self, description, destination)
        self.weight = float(weight.strip('kg'))
    def cost(self):
        return Package.cost(self) + 0.5 * self.weight
    def __str__(self, invoice=False):
        cost = f", Κόστος: {self.cost():.2f}€" if invoice else ""
        return Package.__str__(self) + f"Βάρος: {self.weight}kg{cost}"

class Envelope(Package):
    def __init__(self, description, destination, priority):
        Package.__init__(self, description, destination)
        self.priority = int(priority.strip('προτεραιότητα '))
    def cost(self):
        return Package.cost(self) + 0.20 * self.priority
    def __str__(self, invoice=False):
        cost = f", Κόστος: {self.cost():.2f}€" if invoice else ""
        return Package.__str__(self) + f": Προτεραιότητα {self.priority}{cost}"

class Bulky_Item(Package):
    def __init__(self, description, destination, length, width, height):
        Package.__init__(self, description, destination)
        self.length = float(length.strip('μ').strip(' μήκος '))
        self.width = float(width.strip('μ').strip(' πλάτος '))
        self.height = float(height.strip('μ').strip(' ύψος '))
    def cost(self):
        return Package.cost(self) + 20 * self.length * self.height * self.width
    def __str__(self, invoice=False):
        cost = f", Κόστος: {self.cost():.2f}€" if invoice else ""
        return Package.__str__(self) + f": Διαστάσεις {self.length} x {self.width} x {self.height}m{cost}"
    
items = '''Πακέτο1 (Αθήνα, 20kg),
Πακέτο2 (Θεσσαλονίκη, 10kg),
Πακέτο3 (Αθήνα, 30kg),
Πακέτο4 (Αθήνα, 4.5kg),
Φάκελος1 (Θεσσαλονίκη, προτεραιότητα 1),
Φάκελος2 (Θεσσαλονίκη, προτεραιότητα 3),
ΟγκώδεςΑντικείμενο1 (Αθήνα, μήκος 0.7μ, πλάτος 0.5μ, ύψος 1μ),
ΟγκώδεςΑντικείμενο2 (Θεσσαλονίκη, μήκος 1μ, πλάτος 0.5μ, ύψος 1μ),
ΟγκώδεςΑντικείμενο3 (Αθήνα, μήκος 2μ, πλάτος 0.7μ, ύψος 0.7μ),
'''
def filter(txt):
    return txt.replace("(", ",").replace(")", "").split(",")
packages = [] 
for item in items.split("\n"):
    if 'Πακέτο' in item:
        p =filter(item)
        packages.append(Parcel(*p[:3]))
    elif 'Φάκελος' in item:
        p = filter(item)
        packages.append(Envelope(*p[:3]))
    elif 'ΟγκώδεςΑντικείμενο' in item:
        packages.append(Bulky_Item (*filter(item)[:5]))

## εκτυπώσεις
print('Δελτίο αποστολής')
for p in packages:
    print(p)
print(40*"_"+"\n\n")

print('Τιμολόγιο')
for p in packages:
    print(p.__str__(invoice=True))
print(f"ΣΥΝΟΛΙΚΟ ΚΟΣΤΟΣ: {sum([p.cost() for p in packages]):.2f}€")
print(40*"_"+"\n\n")
