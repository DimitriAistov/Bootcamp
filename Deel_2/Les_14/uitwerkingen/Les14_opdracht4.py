lijst1=[]

for A in range(5):
    item = input('Wat wilt u aan de lijst toevoegen? ')
    lijst1.append(item)

lijst2 = "\n".join(lijst1)
print(lijst2)