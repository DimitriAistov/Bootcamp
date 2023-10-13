import random

green_text = "\033[92m"
red_text = "\033[91m"
reset_text = "\033[0m"

ronden = 0
fouten = 0

while True:
    getal1 = random.randint(1, 5)
    getal2 = None
    
    while getal1 != getal2:
        try:
            getal2 = int(input("Voer een getal tussen 1 en 5 in: "))
            if 1 <= getal2 <= 5:  # Controleer of het ingevoerde getal binnen de range 1-5 ligt
                if getal2 == getal1:
                    print(green_text + "Je hebt het getal goed geraden!" + reset_text)
                else:
                    print(red_text + "Je hebt het getal niet goed geraden!" + reset_text)
            else:
                print(red_text + "Voer een getal in binnen de range 1-5." + reset_text)
        except ValueError:
            print(red_text + "Ongeldige invoer. Voer een geldig getal in." + reset_text)
    
    opnieuw = input("Wil je nog een ronde? (Ja/Nee)")
    if opnieuw.lower() != "ja":
        break
