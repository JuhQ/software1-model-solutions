# monikkotietorakenne
# sijainti       1        2        3       4
# index          0        1        2       3
vuodenajat = ("talvi", "kevät", "kesä", "syksy")

def get_vuodenaika(kuukauden_numero):
    if kuukauden_numero in [12, 1, 2]:
        return vuodenajat[0]
    elif kuukauden_numero in [3,4,5]:
        return vuodenajat[1]
    elif kuukauden_numero in [6,7,8]:
        return vuodenajat[2]
    elif kuukauden_numero in [9, 10, 11]:
        return vuodenajat[3]
    else:
        return "?????"

#    sijainti          1       2      3       4        5       6      7      8     9        10      11      12
#    index             0       1      2       3        4       5       6      7      8     9        10      11
vuodenajat_pitka = ("talvi","talvi","kevät","kevät","kevät","kesä","kesä","kesä","syksy","syksy","syksy","talvi")

def get_vuodenaika2(kuukauden_numero):
    if kuukauden_numero > 12:
        return "?????"
    return vuodenajat_pitka[kuukauden_numero - 1]

def get_arvo():
    return input("Anna kuukauden numero (tyhjä lopettaa): ")

kuukausi_str = get_arvo()
while kuukausi_str != "":
    print(get_vuodenaika(int(kuukausi_str)))
    print(get_vuodenaika2(int(kuukausi_str)))

    kuukausi_str = get_arvo()
