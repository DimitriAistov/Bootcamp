def get_integer(functie1):
    while True:
        try:
            integer1=int(input('Voer een integer in: '))
            return (integer1)
        except ValueError:
            print('Verkeerde input ')
get_integer

def get_float(functie2):
    while True:
        try:
            float1=float(input('Voer een float in: '))
            return (float1)
        except ValueError:
            print('Verkeerde input ')
get_float


integer2 = get_integer('Voer een integer in: ')
float2 = get_float('Voer een float in: ')

print(integer2)
print(float2)
