def calcularIdade(nome,anonNascimeto):
    idade = 2025 - anonNascimeto
    if idade >=18:
        print(f"{nome}, você tem {idade} anos, então é maior de idade")
        return True
    else: 
        print(f"{nome}, você tem {idade} anos, e é menor de idade")
        return False


a = calcularIdade(input("Qual seu nome:") , int(input("Qual ano voce nasceu:")))
b = calcularIdade(input("Qual seu nome:") , int(input("Qual ano voce nasceu:")))
c = calcularIdade(input("Qual seu nome:") , int(input("Qual ano voce nasceu:")))
