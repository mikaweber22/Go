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

# --- Mika's Idee ---
Kursteimehmer_info = {
    "1": ["Mika", 14, "Burger", "Duncan, Ralf, Vincent"],
    "2": ["Lucy", 10, "Nudeln", "Sarah, Mira, Sabina"],
    "3": ["Hanno", 12, "Nudeln", "Anton, Philip, Ben"],
}

# --- Lucy's Idee ---
lucy = [1, 10, "Nudeln", "Sarah, Mira, Sabina"]
mika = [2, 14, "Burger", "Duncan, Ralf, Vincent"]
hanno = [3, 12, "Nudeln", "Anton, Philip, Ben"]
kursteilnehmer = [lucy, mika, hanno]
# ist das gleiche wie oben
kursteilnehmer = [
    [1, "lucy", 10, "Nudeln", "Sarah, Mira, Sabina"],
    [2, "mika", 14, "Burger", "Duncan, Ralf, Vincent"],
    [3, "hanno", 12, "Nudeln", "Anton, Philip, Ben"],
]

# --- Hanno's Idee ---
