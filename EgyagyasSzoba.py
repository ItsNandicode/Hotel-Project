from Szoba_abc import Szoba


# Egyágyas szoba
class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, tengerrenezo=False):
        self._ar = ar
        self.szobaszam = szobaszam
        self.tengerrenezo = tengerrenezo

    @property
    def ar(self):
        return self._ar

    @ar.setter
    def ar(self, ar):
        if ar >= 0:
            self._ar = ar
        else:
            print("Nem lehet negatív ár ")

    def __str__(self):
        extra = ""
        if self.tengerrenezo:
            extra += "Van"
        else:
            extra += "Nincs"

        return f'Egyágyas szoba - Szobaszám: {self.szobaszam}, Ár: {self._ar} Ft/éj, Tengerre néző: {extra}'
