n1= int(input("Digite sua nota 1:"))
n2= int(input("Digite sua nota 2:"))
n3= int(input("Digite sua nota 3:"))
presenca = int(input("Digite sua presença:"))

media = (n1+n2+n3)/3
 
if media >=6 and presenca >= 75:
    print(f"Aprovado pela nota,  {media} vamos ver a presença {presenca}")
else:
    print("Reprovado Malandro")
