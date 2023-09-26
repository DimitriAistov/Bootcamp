omschrijving = ['Uitmuntend', 'Zeer goed', 'Goed', 'Ruim voldoende', 'Voldoende', 'Bijna voldoende', 'Onvoldoende', 'Gering', 'Slecht', 'Zeer slecht','Dit kan ik niet omzetten!']
omschrijving.reverse()

cijfer = int(input('Wat is het cijfer? '))

if cijfer < 0:
    print('Dit kan ik niet omzetten!')
if cijfer >=11:
    print('Dit kan ik niet omzetten!') 

print(omschrijving[cijfer])

if cijfer >5 <=10:
    print('Gefeliciteerd, ', omschrijving[cijfer], 'je resultaat is een ', cijfer)

if cijfer <6:
    print('Jammer', omschrijving[cijfer],' je resultaat is een ', cijfer)