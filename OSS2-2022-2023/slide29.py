li = [10, 5, 125, 44, 2]
min_num = li[0]

for a in li:
    if a < min_num:
        min_num = a

print("Min:", min_num)

# εναλλακτική λύση με την χρήση της συνάρτησης min
print("Min:", min(li))

# εναλλακτική λύση με ταξινόμηση της λίστας
print("Min:", sorted(li)[0])