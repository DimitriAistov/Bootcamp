import random


green_text = "\033[92m"
red_text = "\033[91m"
reset_text = "\033[0m"

for A in range(3):
    getal1 = random.randint(1,5)
    getal2 = None
    
    while getal1 != getal2:
        getal2 = int(input("Voer een getal tussen 1 en 5 in: "))
        
        if getal2 == getal1:
            print(green_text + "Je hebt het getal goed geraden!" + reset_text)
        
        if getal2 != getal1:
            print(red_text +"Je hebt het getal niet goed geraden!" + reset_text )
