class Arbeiter:
    def __init__(self, name, funktion):
        self.name = name
        self.funktion = funktion
        print(f"Hallo! Ich bin {self.name}, zu Ihren Diensten als {self.funktion}!")

    def einkaufen(self, liste):
        for item in liste:
            print(f"Ich kaufe {item}!")

    def winken(self):
        print(f"Hallo, ich bin {self.name}")

liste = ["Eier", "Milch", "stinkende Socken"]
heinz = Arbeiter("Heinz", "Einkäufer")
heinz.einkaufen(liste)

"""
- [x] Funktion in richtiger Form an die richtige Stelle schreiben #M
- [x] eine geeignete Datenstruktur für die Einkaufsliste aussuchen #H
- [x] Einkaufsliste erstellen (3 Items) #H
- [x] neuen Arbeiter erstellen #M
- [x] "Einkaufen"-Funktion mit einem selbst erstellen Arbeiter abrufen #M
- [x] alle Items aus der Einkaufliste, die dem Arbeiter übergeben wird, eines nach dem anderen ausgeben #H
"""