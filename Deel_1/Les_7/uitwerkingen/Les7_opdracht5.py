bank = 10000
jaar = int(input('Na hoeveel jaar wil je de rente weten?'))

for A in range(jaar):
    uitkomst =(bank * (1.028**A))

print (uitkomst)