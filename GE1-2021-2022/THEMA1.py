term = 9         	# ψηφίο βάσης
athroisma = 0		# μεταβλητή αθροίσματος
for i in range(1,10):	# επανάληψη για 9 ψηφία
    athroisma = athroisma + term	# ενημέρωση του αθροίσματος
    term = term*10 + 9	# ενημέρωση του όρου προς πρόσθεση
print(sum)	# εκτύπωση αθροίσματος

# εναλλακτικά
'''Παρατηρούμε ότι το άθροισμα μπορεί να εκφραστεί ως
10-1, 100-1, 1000-1 ... μέχρι 10**9 -1
άρα μπορούμε να εκφράσουμε την ακολουθία των όρων 10**i - 1. 
s = 0 # αρχικό άθροισμα
for i in range(1,10):
    term = 10**i - 1 # όρος αθροίσματος
    s += term # πρόσθεση του νέου όρου στο άρθροισμα
print(s) '''
