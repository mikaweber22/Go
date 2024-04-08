class Arbeiter:
    def __init__(self, name, funktion):
        self.name = name
        self.funktion = funktion
        print(f"Hallo! Ich bin {self.name}, zu Ihren Diensten als {self.funktion}!")

karl = Arbeiter("Karl", "Putzhilfe")