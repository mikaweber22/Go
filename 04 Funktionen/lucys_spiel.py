import random

import daten


def erstelle_satzbausteine():
    subjekt = random.choice(daten.subjekte)
    prädikat_und_objekt = random.choice(daten.prädikate_und_objekte)
    adverbialbestimmungen = random.choice(daten.adverbialbestimmungen)
    abverb = random.choice(daten.adverbien)
    twist = random.choice(daten.twists)
    return subjekt, prädikat_und_objekt, adverbialbestimmungen, abverb, twist


def erstelle_satz(bausteine):
    subjekt, prädikat_und_objekt, adverbialbestimmungen, abverb, twist = bausteine
    satz = (
        subjekt
        + " "
        + prädikat_und_objekt
        + " "
        + adverbialbestimmungen
        + " "
        + abverb
        + ", "
        + twist
        + "."
    )
    return satz


for i in range(5):
    satzbausteine = erstelle_satzbausteine()
    satz = erstelle_satz(satzbausteine)
    print(satz + "\n")

