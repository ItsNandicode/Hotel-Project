from Szoba_abc import Szoba


# Kétágyas szoba
class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, minibar=False):
        self._ar = ar
        self.szobaszam = szobaszam
        self.minibar = minibar

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
        if self.minibar:
            extra += "Van"
        else:
            extra += "Nincs"

        return f'Kétágyas szoba - Szobaszám: {self.szobaszam}, Ár: {self._ar} Ft/éj, Minibár: {extra}'
