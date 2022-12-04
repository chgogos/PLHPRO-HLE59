while True:
    string2test = input("εισάγετε συμβολοσειρά:\n")
    if string2test == "":
        print("\n\nΤέλος του προγράμματος")
        break  # Τερματισμός προγράμματος
    else:
        if string2test == string2test[::-1]:
            print("παλίνδρομη")
        else:
            print("όχι παλίνδρομη")
        # εναλλακτική λύση
        ispalindrome = True
        for i in range(0, int(len(string2test) / 2)):
            if string2test[i] != string2test[len(string2test) - i - 1]:
                ispalindrome = False
        if ispalindrome:
            print("παλίνδρομη")
        else:
            print("όχι παλίνδρομη")
