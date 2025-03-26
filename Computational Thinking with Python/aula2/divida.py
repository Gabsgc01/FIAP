divida = input('Divida (exemplo - 300): ')
juros = 15

divida = float(divida)

aumento = divida*(juros/100)
divida = divida+aumento
print("Sua divida depois de um mes é", divida)

aumento =  divida*(juros/100)
divida = divida+aumento
print("Sua divida depois de dois meses é", divida)

aumento =  divida*(juros/100)
divida = divida+aumento
print("Sua divida depois de tres meses é", divida)