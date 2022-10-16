principal = 1000 # Αρχικό ποσό
rate = 0.05      # Επιτόκιο
numyears = 5     # Χρόνια
year = 1
while year <= numyears:
  principal = principal * (1 + rate)
  print(year, principal)
  year += 1
