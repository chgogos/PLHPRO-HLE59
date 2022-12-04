from math import sin, cos, sqrt, atan2, radians

airport_data = """
Alexandroupoli	40.855869°N 25.956264°E
Athens 37.936389°N 23.947222°E
Chania	35.531667°N 24.149722°E
Chios	38.343056°N 26.140556°E
Corfu 39.601944°N 19.911667°E
Heraklion	35.339722°N 25.180278°E
Kalamata	37.068333°N 22.025556°E
Kavala 40.913333°N 24.619167°E
Kefalonia	38.12°N 20.500278°E
Kos	36.793336°N 27.091667°E
Lemnos	39.917072°N 25.236308°E
Mytilene	39.0567°N 26.5994°E
Paros	37.020833°N 25.113056°E
Rhodes	36.405419°N 28.086192°E
Samos	37.6891°N 26.9116°E
Thessaloniki 40.519722°N 22.970833°E
Zakynthos 37.750833°N 20.884167°E"""

# λίστα στοιχείων αεροδρομίων
airports = []


def process_airports():
    # συνάρτηση που διαβάζει τα στοιχεία αεροδρομίων και γεμίζει τη λίστα airports
    pass


def distance(lat1, lon1, lat2, lon2):
    # υπολογισμός της απόστασης μεταξύ των γεωγραφικών συντεταγμένων lon1, lat1 και
    # των γεωγραφικών συντεταγμένων lon2, lat2 χρησιμοποιώντας τον τύπο Haversine
    # https://en.wikipedia.org/wiki/Haversine_formula

    R = 6373.0  # ακτίνα της γης σε km
    lat1, lon1 = radians(lat1), radians(lon1)
    lat2, lon2 = radians(lat2), radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    d = R * c
    return d


def menu():
    # συνάρτηση που παρουσιάζει το μενού επιλογών και χειρίζεται τις
    # απαντήσεις του χρήστη
    pass


def min_distance():
    # συνάρτηση που υπολογίζει την ελάχιστη μεταξύ των αεροδρομίων της λίστας airports
    pass


### κυρίως πρόγραμμα ###

process_airports()

## επαναληπτική κλήση μενού και διαχείριση απάντησης χρήστη
