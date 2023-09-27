leeftijd = int(input('Wat is uw leeftijd? '))
snor = input('Heeft u een snor? (ja of nee) ')
diploma = input('heeft u een diploma? (ja of nee) ')


if leeftijd >=18 and snor == 'ja':
    print('Je bent aangenomen!')

elif leeftijd <18 and diploma == 'ja':
    print('Je bent aangenomen')

else:
    print('Je bent niet aangenomen.')
