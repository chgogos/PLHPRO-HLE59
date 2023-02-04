# ΕΑΠ- ΘΕ ΠΛΗΠΡΟ - Γραπτή Εργασία 3 - Υπoεργασία 3

from math import sin, cos, sqrt, atan2, radians

data = '''ATH	Athens	37.936389°N 23.947222°E
JTR	Santorini	36.402937°N 23.947222°E
KLX	Kalamata	37.068333°N 22.025556°E
RHO	Rhodes	36.405419°N 28.086192°E
SKG	Thessaloniki	40.519722°N 22.970833°E'''

class Airport():
    '''κλάση αεροδρομίων'''
    airport_dict = {} # λεξικό που περιέχει ως τιμές τα αντικείμενα της κλάσης

    @staticmethod
    def load_airports(f):
        for line in data.split('\n'):
            Airport(*line.strip().split("\t"))

    @staticmethod
    def available_airports():
        airport_list = "Διαθέσιμα αεροδρόμια: "
        for air in Airport.airport_dict:
            airport_list += f"{air}, "
        return airport_list.rstrip(", ")

    def __init__(self, code, name, coordinates):
        self.code = code
        self.name = name
        self.coordinates_str = coordinates
        self.coordinates = [float(x[:-2]) for x in coordinates.split()]
        Airport.airport_dict[code] = self
    
    def __str__(self):
        return f"{self.code}  {self.name}  {self.coordinates_str}"

    def get_distance(self, other):
        '''μέθοδος που υπολογίζει την απόσταση από ένα άλλο αεροδρόμιο'''
        # based on haversine formula https://en.wikipedia.org/wiki/Haversine_formula#cite_note-Gade2010-9
        R = 6373.0   # approximate radius of earth in km
        lat1, lon1 = radians(self.coordinates[0]), radians(self.coordinates[1])
        lat2, lon2 = radians(other.coordinates[0]), radians(other.coordinates[1])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        d = R * c
        return d

class Trip():
    '''Κλάση ταξιδιού, εκτυπώνει τις αποστάσεις των επί μέρους πτήσεων'''    

    def __init__(self, itinerary):
        self.itinerary = itinerary
        self.airports = itinerary.split('-')
        self.total_distance = 0        

    def __str__(self):
        '''εκτυπώνει τη συνολική διαδρομή και τις αποστάσεις των πτήσεων'''
        out = "Υπολογισμός αποστάσεων πτήσης\n"
        self.total_distance = 0
        for i in range(len(self.airports)-1):
            air1 = Airport.airport_dict[self.airports[i]]
            air2 = Airport.airport_dict[self.airports[i+1]]
            flight_distance = air1.get_distance(air2)
            out += f"<{air1.name}, {air2.name}>\t {flight_distance:.2f}\n"
            self.total_distance += flight_distance
        out += f"Συνολική απόσταση: {self.total_distance:.2f}"
        return out

class Menu():
    def __init__(self):
        Airport.load_airports('airports.txt')
        while True:
            print("Παρακαλώ εισάγετε δρομολόγιο ως ακολουθία κωδικών αεροδρομίων, πχ. KLX-ATH-RHO-ATH")
            print(Airport.available_airports())
            itinerary = input(">>")
            if not itinerary: break     
            for x in itinerary.split("-"): 
                if x not in Airport.airport_dict.keys(): break
            else:                
                t = Trip(itinerary)
                print(t)

if __name__ == "__main__": Menu()
