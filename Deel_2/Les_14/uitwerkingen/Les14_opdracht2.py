lijst1 = [1,2,3,4,5]

index = int(input("Voer een getal in "))

if index > 0 and index < len(lijst1):
    getal = lijst1.pop(index)
    print('Het verwijderde getal is: ',getal)
    print('Uw lijst is nu', lijst1)

 