lijst1 = ['kaas','ham','vis','eend','tosti']

woord1 = input('Voer een woord in: ')

if woord1 in lijst1:
    lijst1.remove(woord1)
    print(lijst1)

elif woord1 not in lijst1:
    lijst1.append(woord1)
    print (lijst1)