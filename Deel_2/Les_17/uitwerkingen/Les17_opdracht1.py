getal1 = 3
getal2 = int(input("Voer een getal tussen 1 en 5 in: "))

green_text = "\033[92m"
red_text = "\033[91m"
reset_text = "\033[0m"

if getal2 == getal1:
    print(green_text + "Je hebt het getal goed geraden!" + reset_text)

if getal2 != getal1:
    print(red_text +"Je hebt het getal niet goed geraden!" + reset_text )
