import random

import daten


def satzbausteine():
    subjekt = random.choice(daten.subjekte)
    prädikat_und_objekt = random.choice(daten.prädikate_und_objekte)
    adverbialbestimmungen = random.choice(daten.adverbialbestimmungen)
    abverb = random.choice(daten.adverbien)
    twist = random.choice(daten.twists)
    return subjekt, prädikat_und_objekt, adverbialbestimmungen, abverb, twist


for i in range(5):
    satzbausteine()

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

    print(satz + "\n")
