# ΕΑΠ- ΘΕ ΠΛΗΠΡΟ - Γραπτή Εργασία 3 - Υποεργασία 4

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
    pass #Εδώ συμπληρώνετε τον κώδικά σας

class Envelope(Package):
    pass #Εδώ συμπληρώνετε τον κώδικά σας

class Bulky_Item(Package):
    pass #Εδώ συμπληρώνετε τον κώδικά σας
    
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
