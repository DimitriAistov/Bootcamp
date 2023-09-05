varA = input('Wat is het eerste getal? ')
varB = input('Wat is het tweede getal? ')
varC = input('Wat is het derde getal? ')


if varA > varB and varA > varC:
    print('Variabele 1 is het grootste')
if varB > varA and varB > varC:
    print('Variabele 2 is het grootste')
if varC > varA and varC > varB:
    print('Variabele 3 is het grootste')
if varA == varB and varB == varC:
    print('alle variabelen zijn gelijk')