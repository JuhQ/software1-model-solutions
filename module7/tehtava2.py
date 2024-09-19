def get_nimi():
    return input("Anna nimi (tyhjä lopettaa): ")

nimi = get_nimi()

# joukkotietorakenne
nimet = set()

# huom: {} tyhjänä on dict, ei set
# {'arvo', 'toinen'} taas on set
# python on kivaa

while nimi != "":

    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
    nimet.add(nimi)
    nimi = get_nimi()

for nimi in nimet:
    print(nimi)
