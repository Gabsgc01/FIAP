def pode_Aposentar(sexo, contribuicao, idade):

    if sexo == "mulher" and (contribuicao >=15 and idade >=62):
        print(f"Voce pode Se aposentar, sua idade é {idade}, e tem {contribuicao} anos de contrinuição")
        return True
    elif sexo == "homem" and (contribuicao>=15 and idade >=65):
        print(f"Voce pode Se aposentar, sua idade é {idade}, e tem {contribuicao} anos de contribuição")
        return True 
    else:
        print("Vai trabalhar vagabundo")
        return False 

sexo = input("digite Seu sexo: ")
idade = int(input("Digite sua Idade:"))
contribuicao = int(input("Quantos anos de contribuição:"))

assert(pode_Aposentar("mulher",10,70)==False)
assert(pode_Aposentar("mulher",20,70)==True)
assert(pode_Aposentar("homem",10,50)==False)
assert(pode_Aposentar("homem",12,70)==False)
assert(pode_Aposentar("homem",17,70)==True)

pode_Aposentar(sexo,contribuicao,idade)
