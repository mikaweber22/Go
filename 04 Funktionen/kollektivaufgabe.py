import numpy as np

unsere_fragen = (
    "Wie glücklich bist du heute?",
    "Wie glücklich warst du letzten Monat?",
    "Wie sehr glaubst du an deine Fähigkeit, dein Leben immer besser zu machen?",
)

"""
1. Erstelle eine Funktion, die die Antworten einer Person auf die Fragen speichert und zurückgibt.
2. Erstelle eine Funktion, die den Durchschnitt der Antworten berechnet und zurückgibt.
3. Erstelle eine Funktion, die die Antworten als eine Liste aus Listen in einer Datei speichert.
"""


# 1. Antworten als Liste speichern (mit input()-Funktion)
def antworten_kriegen(fragen):
    anzahl_personen = int(input("Wie viele Personen antworten heute?"))
    antworten = np.zeros((anzahl_personen, len(fragen)))
    for i in range(anzahl_personen):
        for j in range(len(fragen)):
            antwort = float(input(fragen[j]))
            antworten[i, j] = antwort

    return antworten


antworten = antworten_kriegen(unsere_fragen)


# 2. Durchschnitt berechnen
# antworten: [[1,2,3],[4,5,6],[7,8,9]]
def durchschnitt_berechnen(antworten):
    durchschnitte = np.zeros(len(antworten))
    for antwort_einer_person in antworten:
        for i, antwort in enumerate(antwort_einer_person):
            durchschnitte[i] += antwort

    durchschnitte = durchschnitte / len(antworten)

    return durchschnitte


durchschnitte = durchschnitt_berechnen(antworten)


# 3. Antworten als Datei speichern
def in_datei_speichern(durchschnitte):
    datei = open("textdatei.txt", "w")
    datei.write(durchschnitte)
