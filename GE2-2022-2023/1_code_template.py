def dec_to_bin(num):
    num = int(num)
    while num > 0:
        print(num)
        num = num // 2


def bin_to_dec(num):
    pass


def twos_comp(num):
    pass


# ΜΕΝΟΥ
if __name__ == "__main__":
    while True:
        print("Επιλογές")
        print("========")
        print(
            "1. Μετατροπή δεκαδικού αριθμού στο δυαδικό σύστημα, 2. Μετατροπή δυαδικού αριθμού στο δεκαδικό σύστημα, 3. Εύρεση συμπληρώματος δυαδικού αριθμού"
        )
        choice = input("Δώστε την επιλογή σας (enter για έξοδο): ")
        if choice == "":
            break
        if choice == "1":
            x = input("Δώσε αριθμό σε δεκαδική μορφή")
            dec_to_bin(x)
        elif choice == "2":
            pass
        elif choice == "3":
            pass
