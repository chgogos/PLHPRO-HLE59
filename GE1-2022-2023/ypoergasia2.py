# πέτρα-ψαλίδι-χαρτί

counter = 0
machine_symbols = "ΠΧΨΨΠΧΧΧΨΠΠΧΨΨΠΧΧΧΨΠ"  # Αυθαίρετη συμβολοσειρά
while True:
    user_selection = input("διάλεξε (Π)έτρα, (Ψ)αλίδι, (Χ)αρτί:")
    if not user_selection:
        break
    if user_selection not in "ΠΨΧ":  # Αμυντικός Προγραμματισμός
        print("παρακαλώ δώσε κεφαλαίο Π, Ψ, ή Χ")
        continue
    else:
        machine_selection = machine_symbols[counter]
        print("ο υπολογιστής διάλεξε", machine_selection)
        if counter == len(machine_symbols) - 1:
            counter = 0
        else:
            counter += 1
        if machine_selection == user_selection:
            print("Ισοπαλία, διαλέξατε το ίδιο")
            continue
        combination = user_selection + machine_selection
        if combination == "ΠΨ" or combination == "ΨΧ" or combination == "ΧΠ":
            print("Κέρδισες!")
        else:
            print("Έχασες!")
        # είσοδος και έλεγχος για να παίξουν πάλι οι παίκτες
        if str(input("Θέλετε να παιξετε πάλι, (Ν)αι/(Ο)χι;\n")) == "Ν":
            continue
        else:
            print("Τέλος Παιχνιδιού.")
            break  # διακοπή επανάληψης και τερματισμός προγράμματος
