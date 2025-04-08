def podeVotar(nome, idade):
    if idade >= 16:
        print(f"Sim, a pessoa {nome} pode votar")
        return True
    else:
        print(f"Não, a pessoa {nome} ainda não pode votar")
        return False




a = podeVotar(input("Digite seu nome:"),int(input("Digite sua idade:")))
print(f"a primeira resposta foi {a}")
b = podeVotar(input("Digite seu nome:"),int(input("Digite sua idade:")))
print(f"a segunda resposta foi {b}")
c = podeVotar(input("Digite seu nome:"),int(input("Digite sua idade:")))

