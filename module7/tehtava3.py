def get_optiot():
    return input("Anna komento (uusi, hae, lopeta): ")

def luo_uusi_asema(asemat):
    print("Luodaan uusi asema.")
    koodi = input(" - Anna ICAO-koodi: ")
    nimi = input(" - Anna nimi: ")

    asemat[koodi] = nimi


def hae_asema(asemat):
    print("Haetaan asema.")
    hakusana = input(" - Anna ICAO-koodi: ")
    if hakusana not in asemat:
        print(f"ICAO-koodilla {hakusana} ei löytyny asemaa.")
    else:
        print(f"ICAO-koodilla {hakusana} löytyi: {asemat[hakusana]}")

def ohjelma(komento, asemat):
    if komento == "uusi":
        luo_uusi_asema(asemat)
    elif komento == "hae":
        hae_asema(asemat)
    else:
        print("Tuntematon komento")

komento = get_optiot()
asemat = {}
while komento != "lopeta":
    ohjelma(komento, asemat)
    komento = get_optiot()

print("Kiitos näkemiin.")