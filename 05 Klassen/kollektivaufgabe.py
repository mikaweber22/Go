"""
Wir wollen eine Klasse für ein Auto erstellen.
Aufgaben:
1. Erstelle eine Klasse für ein Auto.
2. Erstelle einen Konstruktor, der folgende Attribute erstellt:
- Marke
- Farbe
- maximale Geschwindigkeit
- Beschleunigung (0-100 km/h in Sekunden)
- Baujahr
3. Erstelle ein Auto-Objekt deiner Wahl, indem du die Klasse mit den Werten, die du dir vorstellst, aufrufst.
"""


class Auto:
    def __init__(self, marke, farbe, maximale_geschwindigkeit, beschleunigung, baujahr):
        self.marke = marke
        self.farbe = farbe
        self.geschwindigkeit = 0
        self.maximale_geschwindigkeit = maximale_geschwindigkeit
        self.beschleunigung = beschleunigung
        self.baujahr = baujahr

    def beschleunigen(self):
        if self.geschwindigkeit > self.maximale_geschwindigkeit - 10:
            self.geschwindigkeit = self.maximale_geschwindigkeit
            print("das Auto fährt so schnell wie möglich")
            return
        self.geschwindigkeit = self.geschwindigkeit + 10
        print(f"Das Auto fährt mit {self.geschwindigkeit} km/h.")

    def bremsen(self):
        if self.geschwindigkeit < 10:
            self.geschwindigkeit = 0
            print("Das Auto steht.")
            return
        self.geschwindigkeit = self.geschwindigkeit - 10
        print(f"Das Auto fährt mit {self.geschwindigkeit} km/h.")


auto1 = Auto("Ford", "Silber", 290, 4.4, 1970)
geschwindigkeit = auto1.maximale_geschwindigkeit
print(geschwindigkeit)
