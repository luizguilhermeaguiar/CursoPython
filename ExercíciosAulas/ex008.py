n = float(input('Digite uma distância em metros: '))

print('A medida de {}m corresponde a: \n{}Km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm' .format(n, (n/1000), (n/100),(n/10), (n*10), (n*100), (n*1000)))