def get_integer(functie1):
    integer1=int(input('Voer een integer in: '))
    print (integer1)
get_integer

def get_float(functie2):
    float1=float(input('Voer een float in: '))
    print (float1)
get_float

def getString(functie3):
    string1=str(input('Voer een string in '))
    print (string1)
getString

def get_letter(functie4):
    while True:
        letter1 = input(functie4)
        if len(letter1) == 1 and letter1.isalpha():
            return(letter1.upper())


integer2 = get_integer('Voer een integer in: ')
float2 = get_float('Voer een float in: ')
string2 = getString('Voer een string in: ')
letter = get_letter("Voer een letter in: ")
print(letter)