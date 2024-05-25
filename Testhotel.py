from datetime import datetime
from EgyagyasSzoba import EgyagyasSzoba
from KetagyasSzoba import KetagyasSzoba
from Szalloda import Szalloda
from Foglalas import Foglalas

my_egyszoba = EgyagyasSzoba(10000, 1, True)
my_ketszoba = KetagyasSzoba(20000, 2, True)
my_haromszoba = KetagyasSzoba(20000, 3, True)
szoba_lista = [my_egyszoba, my_ketszoba, my_haromszoba]
my_szaloda = Szalloda("Snowy Palms Hotel", szoba_lista)

foglal = Foglalas(my_szaloda)

# foglal.szoba_ar(my_egyszoba)
foglal.szoba_foglalas(my_egyszoba, datetime(2024, 5, 26))
foglal.szoba_foglalas(my_egyszoba, datetime(2024, 7, 26))
foglal.szoba_foglalas(my_egyszoba, datetime(2024, 6, 26))
foglal.szoba_foglalas(my_ketszoba, datetime(2024, 5, 26))
foglal.szoba_foglalas(my_haromszoba, datetime(2024, 5, 26))

# foglal.ossz_foglalas()

# Interfész
my_szaloda.szaloda_nev()
print()

foglaltak = 0
while True:
    print(f"Üdvözöljük a szobafoglaló alkalmazásban, írja be a kívánt számot: ")
    osz_szobak = my_szaloda.szobak
    szurtszobak = []
    if foglaltak >= 1:
        print()
    hotel_beker = input("Foglalás: 1\nFoglalás lemondása: 2\nlistázás: 3\nKilépés: 4\nMelyiket szeretné választani? ")

    if hotel_beker == "4":
        print("kilépés")
        break
    print()
    snack = 0
    ev = 0
    ho = 0
    nap = 0
    tenger = 0
    lefoglalt_szoba = None
    if hotel_beker == "1":
        szoba = input("Egyágyas: 1\n"
                      "Kétágyas: 2\n"
                      "Milyen szobát szeretne foglalni: ")
        if szoba == "1":
            print()
            tengere_nezo_e = input("igen/nem\n"
                                   "Legyen tengerre nező? ")
            if tengere_nezo_e == "igen":
                tenger = True
            elif tengere_nezo_e == "nem":
                tenger = False
            else:
                print()
                print("Csak Nem és Igen megengedett!")
                break

            print()
            print("Találatok: ")
            for sz in osz_szobak:
                if isinstance(sz, EgyagyasSzoba) and sz.tengerrenezo == tenger:
                    szurtszobak.append(sz)
            for sz in szurtszobak:
                print(sz)

            datum = input("Mikor legyen? YYYY-MM-DD : ")
            if datum.isalpha():
                print()
                print("Csak Érvényes dátumot lehet be írni! ")
                break
            if datum.isdigit():
                print()
                print("Csak Érvényes dátumot lehet be írni! ")
                break

            normal_datum = datum.split("-")
            ev = int(normal_datum[0])
            ho = normal_datum[1]
            if ho[0] == "0":
                ho = int(ho[1])
            else:
                ho = int(ho)
            nap = normal_datum[2]
            if nap[0] == "0":
                nap = int(nap[1])
            else:
                nap = int(nap)
            # szoba_lista.append(szoba1)

            foglaltak += 1

        if szoba == "2":
            print()
            minibar = input("igen/nem\n"
                            "Legyen minibár? ")
            if minibar == "igen":
                snack = True
            elif minibar == "nem":
                snack = False
            else:
                print()
                print("Csak Nem és Igent lehet írni!")
                break

            print()
            print("Találatok: ")
            for sz in osz_szobak:
                if isinstance(sz, KetagyasSzoba) and sz.minibar == snack:
                    szurtszobak.append(sz)
            for sz in szurtszobak:
                print(sz)

            datum = input("Mikor legyen? YYYY-MM-DD :  ")
            if datum.isalpha():
                print()
                print("Csak Érvényes dátumot lehet be írni! ")
                break
            if datum.isdigit():
                print()
                print("Csak Érvényes dátumot lehet be írni! ")
                break
            normal_datum = datum.split("-")
            ev = int(normal_datum[0])
            ho = normal_datum[1]
            if ho[0] == "0":
                ho = int(ho[1])
            else:
                ho = int(ho)
            nap = normal_datum[2]
            if nap[0] == "0":
                nap = int(nap[1])
            else:
                nap = int(nap)

            foglaltak += 1
        else:
            print("Csak érvényes számot lehet beírni!")
            break
        # sikeres = False
        for sz in szurtszobak:
            try:
                if foglal.szoba_foglalas(sz, datetime(ev, ho, nap)):
                    print()
                    print(f"Sikeres foglalás, a szoba száma:  {sz.szobaszam}")
                    foglal.szoba_ar(sz)
                    sikeres = True
                    lefoglalt_szoba = sz
                    break

                else:
                    print()
                    print("Sikertelen foglalás")
                    sikeres = False
                    break
            except:
                print()
                print("Csak Érvényes dátumot lehet be írni! ")
                break

    elif hotel_beker == "3":
        foglaltak += 1
        foglal.ossz_foglalas()

    elif hotel_beker == "2":
        foglal.ossz_foglalas()
        lemondot_szoba = input("Hányas számú szobát szeretné lemonadi: ")
        if str(lemondot_szoba).isalpha():
            print("Csak számot lehet írni! ")
            break

        torolhetp_szoba = False
        for i in foglal.lefoglalt_szobak:
            if int(i["szoba"].szobaszam) == int(lemondot_szoba):
                print(i["szoba"], i["datum"])
                torolhetp_szoba = True

        if not torolhetp_szoba:
            print("Nincs ilyen szobaszám a listában! ")
            break
        lemondot_datum = input("Meylik dátumot szeretné lemondani? YYYY-MM-DD : ")

        if lemondot_datum.isalpha():
            print()
            print("Csak Érvényes dátumot lehet be írni! ")
            break
        if lemondot_datum.isdigit():
            print("Csak Érvényes dátumot lehet be írni! ")
            break

        lemondot_normal_datum = lemondot_datum.split("-")
        lemondot_ev = int(lemondot_normal_datum[0])
        lemondot_ho = lemondot_normal_datum[1]
        if lemondot_ho[0] == "0":
            lemondot_ho = int(lemondot_ho[1])
        else:
            lemondot_ho = int(lemondot_ho)
        lemondot_nap = lemondot_normal_datum[2]
        if lemondot_nap[0] == "0":
            lemondot_nap = int(lemondot_nap[1])
        else:
            lemondot_nap = int(lemondot_nap)
        try:
            lemondott_datum = datetime(lemondot_ev, lemondot_ho, lemondot_nap)
        except:
            print()
            print("Csak Érvényes dátumot lehet be írni! ")
            break

        sikeres_lemondas = False
        for sz in foglal.lefoglalt_szobak:
            if int(sz["szoba"].szobaszam) == lemondot_szoba and sz["datum"] == lemondott_datum:
                foglal.foglalas_lemondas(sz["szoba"], lemondott_datum)
                print()
            print(f"Sikeres lemondás, a szoba száma:  {sz['szoba'].szobaszam}")
            sikeres_lemondas = True
            break
        else:
            print()

        if not sikeres_lemondas:
            print(f"Sikertelen lemondás, erre a szobára erre a napra nincs foglalás")

    elif not hotel_beker.isdigit():
        print()
        print("Csak számokat lehet írni! ")

    else:
        print()
        print("Nincsen ilyen opció, válaszon másik számot! ")
