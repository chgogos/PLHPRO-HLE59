import numpy as np # Χρήση της βιβλιοθήκης numpy
import time as tm # Χρήση της βιβλιοθήκης time

def internalProduct(v1,v2):
    '''Τυπική υλοποίηση εσωτερικού γινομένου διανυσμάτων.'''
    # Υποερώτημα α
    #
    # Υπολογισμός του γινομένου των v1 και v2 με την τυπική 
    # υλοποίηση
    d = 0
    for i in range(len(v1)):
        d += v1[i]* v2[i]
    return d

def internalProduct_np(v1,v2):
    # Υποερώτημα β
    #
    # Υπολογισμός του γινομένου των v1 και v2 με κλήση της dot() της numpy
    return np.dot(v1, v2)

def timeit(mode, rep,v1,v2):
    '''Χρονομέτρηση επαναληπτικού υπολογισμού εσωτερικού γινομένου με την τυπική υλοποίηση'''
    # Αποθήκευση στην μεταβλητή start του χρόνο έναρξης του επαναληπτικού 
    # υπολογισμού με την τυπική υλοποίηση του πολλαπλασιασμού διανυσμάτων 
    start_time = tm.perf_counter()
    # Επανάληψη πολλές φορές, ώστε η ακρίβεια του ρολογιού να μην επηρεάζει 
    # το αποτέλεσμα
    # Υποερώτημα γ
    for _ in range(rep):
        # Κλήση της συνάρτησης, για τον υπολογισμό του γινομένου των v1 και v2
        if mode == "τυπική υλοποίηση":
            prod = internalProduct(v1,v2)
        else:
            prod = internalProduct_np(v1,v2)
    # Εμφάνιση του αποτελέσματος
    print (f"Εσωτερικό γινόμενο διανυσμάτων ({mode}): {prod}")
    # Αποθήκευση στην μεταβλητή finish_time του χρόνου ολοκλήρωσης του 
    # υπολογισμού
    finish_time = tm.perf_counter()
    # Επιστροφή χρονικού διαστήματος 
    return finish_time-start_time

# Κυρίως πρόγραμμα

# Aρχικοποίηση παραμέτρων
random_num_range = 100 # το εύρος των παραγόμενων τυχαίων αριθμών
vector_size = 10000 # το πλήθος των στοιχείων ενός διανύσματος
repetitions = 5000 # ο αριθμός επαναλήψεων του υπολογισμού
# Αρχικοποίηση δύο διανυσμάτων, v1 και v2, με τυχαίους αριθμούς 
v1 = np.random.randint(random_num_range,size=vector_size)
v2 = np.random.randint(random_num_range,size=vector_size)

# Υποερώτημα δ

# Υπολογισμός και εμφάνιση χρόνων αναμονής
t = []
for mode in ["τυπική υλοποίηση", "numpy"]:
    print("\n", f"Υπολογισμός με {mode}. Παρακαλώ περιμένετε ...")
    # Χρονομέτρηση και εμφάνιση του χρόνου εκτέλεσης του επαναληπτικού
    # υπολογισμού με την τυπική υλοποίηση και με την numpy
    t.append(timeit(mode, repetitions,v1,v2)) 
    print(f"χρόνος ({mode}) = {t[-1]:0.5f}")

# Υπολογισμός και εμφάνιση του λόγου των χρόνων εκτέλεσης
ratio = t[0]/t[1]
print(f"H numpy είναι {ratio:0.1f} φορές γρηγορότερη")
