class Kuchen:
    def __init__(self, name):
        self.name = name
        self.gebacken = False
        print(f"{self.name} wurde erstellt.")
    
    def get_name(self):
        return self.name

    def backen(self):
        self.gebacken = True
        print(f"{self.name} ist fertig!")

erdbeerkuchen = Kuchen("Erdbeerkuchen")
erdbeerkuchen.backen()
