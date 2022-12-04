kostos_metaforas1 = 2.0  # μεταφορικά πρώτου βιβλίου
kostos_metaforas2 = 1.0  # μεταφορικά υπόλοιπων βιβλίων
ekptosi = 0.8  # έκπτωση
# Εισαγωγή αριθμού βιβλίων και κόστους βιβλίου
while True:
    try:  # χρήση try ως αμυντικός προγραμματισμός για είσοδο
        vivlia = int(input("Αριθμός βιβλίων: "))
        kostos_vivliou = float(input("Κόστος ενός βιβλίου: "))
        if vivlia > 0 and kostos_vivliou > 0:
            break
        else:
            print("Παρακαλώ δώστε θετικό αριθμό")
    except ValueError:  # σε περίπτωση με έγκυρης εισόδου
        print("Το πλήθος βιβλίων πρέπει να είναι θετικός ακέραιος και το κόστος βιβλίου θετικός αριθμός.")
# υπολογισμός και εκτύπωση συνολικού κόστους παραγγελίας
kostos = vivlia * kostos_vivliou * ekptosi + kostos_metaforas1 + kostos_metaforas2 * (vivlia - 1)
print(f"Κόστος παραγγελίας = {kostos:.2f} €")
