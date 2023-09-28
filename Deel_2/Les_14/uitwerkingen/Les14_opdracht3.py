fruit1 = ["appel", "banaan", "kiwi","sinaasappel"]
fruit2 = input("welke fruit moet worden verwijdert: ")

if fruit2 in fruit1:
    fruit1.remove(fruit2)

else:
    print(fruit2,'komt niet voor in de lijst.')

print("Nieuwe lijst: ")
for fruit3 in fruit1:
    print(fruit3)