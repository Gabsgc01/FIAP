def eh_mapa(mapa):
    if not mapa:
        return False
    

    for elemento in mapa:
        if elemento not in ['.', 'o']:
            return False
    
    return True

assert eh_mapa(['.', '.', '.','o']) == True, "Deve retornar True para mapa com apenas pontos"
assert eh_mapa(['o', 'o', 'o','.']) == True, "Deve retornar True para mapa com apenas 'o'"
assert eh_mapa(['.', 'o', '.']) == True, "Deve retornar True para mapa misturado"
assert eh_mapa([]) == False, "Deve retornar False para lista vazia"
assert eh_mapa(['.', 'x', '.']) == False, "Deve retornar False para caracteres inválidos"

print("Passou todos os testes!")
