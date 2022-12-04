import random

# Ερώτημα α
def generate_random_floats(n, m, seed=0):
    # συνάρτηση που επιστρέφει λίστα n τυχαίων αριθμών στη διάστημα
    # -m, m με σπόρο γεννήτριας ψευδοτυχαίων αριθμών seed (προαιρετικό όρισμα)
    if seed:
        random.seed(seed)
    random_list = []
    for _ in range(n):
        random_list.append(random.uniform(-m, m))
    return random_list


# Ερώτημα β
def find_max_gap(random_list):
    # συνάρτηση  που δέχεται λίστα πραγματικών αριθμών και επιστρέφει τη
    # μέγιστη απόσταση μεταξύ τους
    random_list.sort()
    max_gap = 0
    for i in range(1, len(random_list)):
        if random_list[i] - random_list[i - 1] > max_gap:
            max_gap = random_list[i] - random_list[i - 1]
    return max_gap


# Ερώτημα γ
def present_list(random_list):
    # βοηθητική συνάρτηση που τυπώνει τα στοιχεία μιας λίστας
    print("Η τυχαία λίστα είναι: ", end="")
    for item in random_list[:-1]:
        print("{:.2f},  ".format(item), end="")
    print("{:.2f}".format(random_list[-1]))


### κυρίως πρόγραμμα ###

# Ερώτημα δ
# ζήτησε από τον χρήστη το πλήθος των τυχαίων αριθμών
n = 0
while n == 0:
    reply = input("Δώσε πλήθος τυχαίων αριθμών=")
    if reply.strip().isdigit() and int(reply) > 1:
        n = int(reply)

# ζήτησε από τον χρήστη το διάστημα -m, m
m = 0
while m == 0:
    reply = input("Δώσε το εύρος τιμών [-m, +m]. m=")
    if reply.strip().isdigit() and int(reply) > 0:
        m = int(reply)

# ζήτησε από τον χρήστη την τιμή του σπόρου seed
while True:
    try:
        reply = input(
            "Δώσε τον σπόρο seed (0 για να μη χρησιμοποιηθεί seed από τον χρήστη)="
        )
        seed = int(reply)
        break
    except ValueError:
        pass  # δεν δόθηκε ακέραιος

# Ερώτημα ε
# δημιουργία λίστας τυχαίων αριθμών
random_list = generate_random_floats(n, m, seed)

# # παρουσίαση της λίστας
present_list(random_list)

# υπολογισμός μέγιστης απόστασης
print("Η μέγιστη απόσταση είναι: {:.2f}".format(find_max_gap(random_list)))
