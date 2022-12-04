employees = """Γιώργος Γεωργίου,m,eng,project1 project3 
 Μαρία Ρήγα,f,eng,project2 
 Κατερίνα Σελή,f,secr,project1 project2 
 Νίκος Πάλης,m,tech,project2 
 Λίνα Πενταγιά,f,eng,project1 
 Ρένα Ντορ,f,secr,project3 project2 
 Τζον Κλης,m,tech,project1 project2 
 Λάκης Λαζός,m,eng,project2 
 Μαρίνα Μαρή,f,eng,project3 
 Ζήσης Χελάς,m,tech,project1 project2"""

# αρχικοποίηση των συνόλων


def load_sets():
    # φόρτωμα των στοιχείων του πίνακα εργαζομένων στα σύνολα
    pass


# εκτύπωση set
def show_set(hint, s):
    # βοηθητική συνάρτηση εκτύπωσης συνόλου s με εξήγηση hint
    pass


# ΑΠΑΝΤΗΣΕΙΣ ΣΤΑ ΕΡΩΤΗΜΑΤΑ
# οι άνδρες που δουλεύουν στο project1
def men_project1():
    pass


# όλοι όσοι δουλεύουν στο project1 αλλά όχι στο project2 ή project3
def project1_not_project2_not_project3():
    pass


# οι γυναίκες μηχανικοί
def f_eng():
    pass


# όλοι οι τεχνικοί που δουλεύουν είτε στο project1 ή στο project2
def tech_p1_p2():
    pass


# οι άνδρες μηχανικοί που δεν δουλεύουν στο project2
def m_eng_not_p2():
    pass


#### κυρίως πρόγραμμα ####
# αρχικά σύνολα


### κλήση συναρτήσεων
print("ΑΠΑΝΤΗΣΕΙΣ ΣΤΑ ΕΡΩΤΗΜΑΤΑ:")
men_project1()
project1_not_project2_not_project3()
f_eng()
tech_p1_p2()
m_eng_not_p2()
