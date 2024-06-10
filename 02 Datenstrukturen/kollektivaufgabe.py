# Erstelle die sinnvollste Datenstruktur aus den Datenstruktur-Typen, die wir kennengelernt haben, für folgendes Problem:
# Wir wollen alle Kursteilnehmer auf eine Weise einspeichern, die uns all die Möglichkeiten gibt, die wir brauchen.

# Wir wollen folgende Eigenschaften pro Kursteilnehmer speichern:
# - Teilnehmer-ID
# - Vorname
# - Alter
# - Lieblingsessen
# - Vornamen der drei besten Freunde


"""Aufgaben:
1. Was muss unsere Datenstruktur können?
- wir müssen die Informationen der Kursteilehmer ändern können
- wir müssen neue Teilnehmer hinzufügen können
2. In welcher Datenstruktur können wir einzelne Kursteilnehmer einspeichern?
3. In welcher Datenstruktur können wir alle Kursteilnehmer einspeichern?
"""

kursteilnehmer_paul = [
    {
        "id": 1,
        "name": "Lucy",
        "alter": 10,
        "lieblingsessen": "Nudeln",
        "freunde": ["Sarah", "Mira", "Sabina"],
    },
    {
        "id": 2,
        "name": "Mika",
        "alter": 14,
        "lieblingsessen": "Burger",
        "freunde": ["Duncan", "Ralf", "Vincent"],
    },
    {
        "id": 3,
        "name": "Hanno",
        "alter": 12,
        "lieblingsessen": "Nudeln",
        "freunde": ["Anton", "Philip", "Ben"],
    },
]

kursteilnehmer_mika = {
    "1": ["Mika", 14, "Burger", "Duncan, Ralf, Vincent"],
    "2": ["Lucy", 10, "Nudeln", "Sarah, Mira, Sabina"],
    "3": ["Hanno", 12, "Nudeln", "Anton, Philip, Ben"],
}

kursteilnehmer_lucy = [
    [1, "lucy", 10, "Nudeln", "Sarah, Mira, Sabina"],
    [2, "mika", 14, "Burger", "Duncan, Ralf, Vincent"],
    [3, "hanno", 12, "Nudeln", "Anton, Philip, Ben"],
]

""""
Kollektivaufgabe:
1. Erstelle einen for-Loop für Mika's Idee, der den Namen aller Kursteilnehmer ausgibt.
2. Erstelle einen for-Loop für Paul's Idee, der das Lieblingsessen aller Kursteilnehmer ausgibt.
3. Erstelle einen for-Loop für Lucy's Idee, der das Alter aller Kursteilnehmer ausgibt.
"""

# Beispiel für for-Loop
# zahlen = [1, 2, 3, 4, 5]
# for sdghfgj in zahlen:
#     print(sdghfgj)

# Hanno: Lucy's Idee
print("\n Hanno's Idee")
kursteilnehmer_lucy = [
    [1, "lucy", 10, "Nudeln", "Sarah, Mira, Sabina"],
    [2, "mika", 14, "Burger", "Duncan, Ralf, Vincent"],
    [3, "hanno", 12, "Nudeln", "Anton, Philip, Ben"],
]
for teilnehmer in kursteilnehmer_lucy:
    print(teilnehmer)


# Mika: Mika's Idee
# print("\n Mika's Idee")
# for i in kursteilnehmer_mika:
#     if kursteilnehmer_mika["1"] or kursteilnehmer_mika["2"] or kursteilnehmer_mika["3"]:
#         print(kursteilnehmer_mika["1"]["2"]["3"][1])


# Lucy: Paul's Idee
print("\n Lucy's Idee")
for kursteilnehmer in kursteilnehmer_paul:
    # kursteilnehmer ist ein Dictionary
    # Deshalb rufen wir die Werte mit den Schlüsseln ab
    lieblingsessen = kursteilnehmer["lieblingsessen"]
    print(lieblingsessen)
