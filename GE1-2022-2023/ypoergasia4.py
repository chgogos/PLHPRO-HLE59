"""
up-down-left-right, κενό: τέλος
εντολές u1 d2 l3 r1
"""
while True:
    dim = input("Δώστε διάσταση χώρου n :")
    if dim.isdigit() and int(dim) > 0:
        dim = int(dim)
        break
    print("Παρακαλώ δώστε θετικό ακέραιο αριθμό")
print(
    f"\nΤο ρομπότ θα κινείται σε χώρο {dim} x {dim} (0...{dim-1}, 0...,{dim-1}). Η αρχική του θέση είναι (0,0)"
)
command = "s"
n = dim - 1
x = 0
y = 0
while command != " ":
    command = input(
        "\nΔώστε αριθμό βημάτων και κίνηση πάνω, κάτω, αριστερά δεξιά, πχ. r5, ή κενό χαρακτήρα για τερματισμό:"
    )
    if not command:
        continue
    direction = command[0].lower()
    if direction != "u" and direction != "d" and direction != "l" and direction != "r":
        continue
    step = int(command[1:])
    xtemp, ytemp = x, y
    if direction == "l":
        ytemp = y - step
    elif direction == "r":
        ytemp = y + step
    elif direction == "u":
        xtemp = x - step
    elif direction == "d":
        xtemp = x + step

    if ((xtemp < 0) or (xtemp > n) or (ytemp < 0) or (ytemp > n)):
        print("\n ΣΦΑΛΜΑ! κίνηση έξω από τα όρια του χώρου. ")
        print(f"Η θέση του ρομποτ παραμένει {x}, {y}")
    else:
        x, y = xtemp, ytemp
        print(f"\nH νέα θέση του ρομποτ είναι {x}, {y}")
print("\n\nΤερματισμός προγράμματος")
