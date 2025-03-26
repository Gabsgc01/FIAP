hora_ = int(input("que horas são agora:"))
passou = int(input("quantos minutos passaram?:"))
atual = (minuto_inicial+passou)%60
nova_hora = (minuto_inicial+passou)//60

print("Agora são", nova_hora,":", atual)

