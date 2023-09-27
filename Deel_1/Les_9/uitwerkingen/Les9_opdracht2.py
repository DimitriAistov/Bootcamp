getal = int(input('Kies een getal '))

restA = getal%7
restB = getal%11

if restA or restB >=1:
    print('Dit getal is niet zonder rest deelbaar door 7 en 11')
elif restA or restB ==0:
    print('Dit getal is zonder rest deelbaar door 7 en 11')
