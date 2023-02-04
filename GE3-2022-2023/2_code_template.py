class Camera: # Κλάση Camera
    def __init__(self, location):  # Ζητείται να αρχικοποιήσετε τη συνάρτηση του αντικειμένου Camera
        pass

    def power(self):  # Ζητείται να δημιουργήσετε τη μέθοδο που ενεργοποιεί ή απενεργοποιεί την Camera
        pass

    def zoomUp(self):  # Ζητείται να δημιουργήσετε τη μέθοδο που αυξάνει το zoom της Camera
        pass

    def zoomDown(self):  # Ζητείται να δημιουργήσετε τη μέθοδο που μειώνει το zoom της Camera
        pass

    def nightVision(self):  # Ζητείται να δημιουργήσετε τη μέθοδο που ενεργοποιεί ή απενεργοποιεί τη λειτουργία νυχτερινής όρασης της Camera
        pass

    def __str__(self):  # Μέθοδος αποτύπωσης των συγκεντρωτικών πληροφοριών για όλες τις λειτουργίες της Camera
        out = f'Στοιχεία Κάμερας:\n\tΤοποθεσία: {self.location}\n'
        out += f"\tΚατάσταση κάμερας: {'σε λειτουργία' if self.operation else 'απενεργοποιημένη'}\n"
        if self.operation:
            out += f"\tzoom: {self.zoom}\n"
            out += f"{'(νυχτερινή όραση)' if self.night_vision else ''}\n"
        return out


class Panel(): # Κλάση πίνακα ελέγχου
    def __init__(self): # Ζητείται να δημιουργήσετε μια λίστα με αντικείμενα τύπου Camera
        pass
        
    def select_camera(self): # Ζητείται να δημιουργήσετε τη μέθοδο που επιτρέπει στον χρήστη να επιλέξει τη Camera την οποία θα ελέγξει
        pass

    def control_panel(self): # Mέθοδος για έλεγχο της επιλεγμένης Camera (power, zoom, night_vision)
        while True:
            print(f"\nΠανελ ελέγχου κάμερας {self.camera.location}")
            print(self.camera)
            sel = input('o(on/off), (z)oom (+/-), (n)(yes/no), <enter>: exit:').strip()
            if not sel: break
            if sel[0].lower() == "z":
                if sel[-1] == "+": self.camera.zoomUp()
                if sel[-1] == "-": self.camera.zoomDown()
            elif sel[0].lower() == "n":
                self.camera.nightVision()
            elif sel[0].lower() == "o":
                self.camera.power()


Panel()
