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
        self.maximale_geschwindigkeit = maximale_geschwindigkeit
        self.beschleunigung = beschleunigung
        self.baujahr = baujahr


auto1 = Auto("Ford", "Silber", 290, 4.4, 1970)
geschwindigkeit = auto1.maximale_geschwindigkeit
print(geschwindigkeit)