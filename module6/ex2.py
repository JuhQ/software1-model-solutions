import random

def satunnainen(max):
    return random.randint(1,max)

maksimi = input("Anna maksimi silmäluku: ")

# if -lauseke eroaa tehtävänannosta hieman
# estetään ohjelman kaatuminen
if maksimi == "":
    maksimi = 6
else:
    maksimi = int(maksimi)

while True:
    luku = satunnainen(maksimi)
    print(f"Silmäluku {luku}")
    if luku == 6:
        break
