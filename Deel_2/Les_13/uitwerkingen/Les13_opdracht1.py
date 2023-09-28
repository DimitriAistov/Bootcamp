kleuren = ('blauw', 'rood','geel','groen','oranje','paars')

naam = input('Wat is je naam? ')
kleur = input('Wat is je favoriete kleur? ')


if kleur in kleuren:
    print('Hallo ',naam,'! Uw favoriete kleur is ',kleur,' wat leuk.')

else:
    print('Deze kleur is niet zo geweldig!')