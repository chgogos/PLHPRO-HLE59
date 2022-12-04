epafes = {}
while True:
    reply = input("πατήστε + για νέα επαφή, ? για λίστα επαφών\n>>>")
    if not reply:
        break
    if reply == "+":
        name = input("όνομα:")
        phone = input("τηλέφωνο:")
        if name and phone:
            epafes[name] = phone
        else:
            print("παρακαλώ δώστε στοιχεία")
    elif reply == "?":
        for e in sorted(epafes):
            print("{}: {}".format(e, epafes[e]))
