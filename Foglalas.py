from datetime import datetime


# Foglalás
class Foglalas:
    def __init__(self, szaloda):
        self.lefoglalt_szobak = []
        self.szobak = szaloda.szobak

    @staticmethod
    def szoba_ar(szoba):
        return print(f"Ár : {szoba.ar} ft")

    def szoba_foglalas(self, szoba, datum: datetime):
        # dátumellenőrzés
        mai_datum = datetime.today()
        if datum <= mai_datum:
            print("Múlt időben nem lehet foglalni")
            return False

        # szobaellenőrzés
        vanilyenszoba = False
        for i in self.szobak:
            if szoba == i:
                vanilyenszoba = True
        if not vanilyenszoba:
            print("Nincs ilyen szoba")
            return False

        # foglaltság ellenőrzés
        foglalt = False
        for foglalas in self.lefoglalt_szobak:
            if foglalas["szoba"] == szoba and foglalas["datum"] == datum:
                foglalt = True

        if not foglalt:
            # print("Sikeres foglalás")
            # print(f"Ár : {szoba.ar} ft")
            self.lefoglalt_szobak.append({"szoba": szoba, "datum": datum})
            return True
        else:
            print("Az adott napon foglalt az adott szoba")
            return False

    def foglalas_lemondas(self, szoba, datum: datetime):
        # dátumellenőrzés
        mai_datum = datetime.today()
        if datum < mai_datum:
            print("Múlt időben nem lehet lemondani")
            return

        # szobaellenőrzés
        vanilyenszoba = False
        for i in self.szobak:
            if szoba == i:
                vanilyenszoba = True
        if not vanilyenszoba:
            print("Nem létetik ilyen szoba")
            return

        # foglaltság ellenőrzés
        foglalt = False
        for foglalas in self.lefoglalt_szobak:
            if foglalas["szoba"] == szoba and foglalas["datum"] == datum:
                foglalt = True

        if foglalt:
            # print("Foglalás lemondása")
            self.lefoglalt_szobak.remove({"szoba": szoba, "datum": datum})
            return
        else:
            print("Az adott napon foglalt az adott szoba")
            return

    def ossz_foglalas(self):
        print("Összes lefoglalt szoba: ")

        for i in self.lefoglalt_szobak:
            print(f"{i["szoba"]} - Dátum: {i["datum"].strftime("%Y-%m-%d")}")
