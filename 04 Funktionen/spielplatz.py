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
    subjekt, prädikat_und_objekt, adverbialbestimmungen, abverb, twist = satzbausteine()

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


def baue_haus(ziegel, steine, farbe):
    print(
        f"Ich baue ein Haus mit {ziegel} Ziegeln, {steine} Steinen und {farbe} Farbe."
    )

    wand1 = "Erste Wand aus " + ziegel + " Ziegeln"
    wand2 = "Zweite Wand aus " + steine + " Steinen"
    wand3 = "Dritte Wand aus " + farbe + " Farbe"
    haus = wand1 + " " + wand2 + " " + wand3

    return haus



haus = baue_haus("Ziegel", "Steine", "Farbe")
