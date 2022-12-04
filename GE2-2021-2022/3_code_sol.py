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
m = set()
f = set()
eng = set()
tech = set()
secr = set()
p1 = set()
p2 = set()
p3 = set()

# ερώτημα α
def load_sets():
    # φόρτωμα των στοιχείων της συμβολοσειράς εργαζομένων στα σύνολα
    for emp in employees.split("\n"):
        if emp:
            e = emp.split(",")
            name = e[0]
            gender = e[1]
            role = e[2]
            projects = e[3].split()
            if "m" in gender:
                m.add(name)
            elif "f" in gender:
                f.add(name)
            if "secr" in role:
                secr.add(name)
            elif "eng" in role:
                eng.add(name)
            elif "tech" in role:
                tech.add(name)
            if "project1" in projects:
                p1.add(name)
            if "project2" in projects:
                p2.add(name)
            if "project3" in projects:
                p3.add(name)


# ερώτημα β
def show_set(hint, s):
    # βοηθητική συνάρτηση εκτύπωσης συνόλου s με εξήγηση hint
    print(hint)
    for member in s:
        print(member, end=" ")
    print()


# ΑΠΑΝΤΗΣΕΙΣ ΣΤΑ ΕΡΩΤΗΜΑΤΑ
# οι άνδρες που δουλεύουν στο project1
def men_project1():
    show_set("οι άνδρες που δουλεύουν στο project1 είναι:", m.intersection(p1))


# όλοι όσοι δουλεύουν στο project1 αλλά όχι στο project2 ή project3
def project1_not_project2_not_project3():
    show_set(
        "όσοι δουλεύουν στο project1 και όχι στα project2, 3 είναι:",
        p1.difference(p2).difference(p3),
    )


# οι γυναίκες μηχανικοί
def f_eng():
    show_set("οι γυναίκες μηχανικοί είναι:", f.intersection(eng))


# όλοι οι τεχνικοί που δουλεύουν είτε στο project1 ή στο project2
def tech_p1_p2():
    show_set(
        "οι τεχνικοί που δουλεύουν είτε στο project1 ή στο project2 είναι:",
        tech.intersection(p1.union(p2)),
    )


# οι άνδρες μηχανικοί που δεν δουλεύουν στο project2
def m_eng_not_p2():
    show_set(
        "οι άνδρες μηχανικοί που δεν δουλεύουν στο project2 είναι:",
        m.intersection(eng).difference(p2),
    )


#### κυρίως πρόγραμμα ####
# ερώτημα γ
# εμφάνιση των αρχικών συνόλων
load_sets()
show_set("οι άνδρες είναι:", m)
show_set("οι γυναίκες είναι:", f)
show_set("οι μηχανικοί είναι:", eng)
show_set("οι διοικητικοί υπάλληλοι είναι:", secr)
show_set("οι τεχνικοί είναι:", tech)
show_set("οι εργαζόμενοι στο project1 είναι:", p1)
show_set("οι εργαζόμενοι στο project2 είναι:", p2)
show_set("οι εργαζόμενοι στο project3 είναι:", p3)
### κλήση συναρτήσεων
# ερωτήματα γ1 - γ5
print("ΑΠΑΝΤΗΣΕΙΣ ΣΤΑ ΕΡΩΤΗΜΑΤΑ:")
men_project1()
project1_not_project2_not_project3()
f_eng()
tech_p1_p2()
m_eng_not_p2()
