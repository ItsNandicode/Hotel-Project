class Szalloda:
    def __init__(self, nev: str, szobak: list):
        self.szobak = szobak
        self.nev = nev

    def print_adatok(self):
        for i in self.szobak:
            print(i)

    def szaloda_nev(self):
        print(self.nev)
