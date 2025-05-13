def nomes_muito_grandes(lista_nomes):
    lista=[]
  
    for nome in lista_nomes:
        tamanho_nome= len(nome)
        if tamanho_nome>10:
            lista.append(nome)
    return lista
    

# Testes
assert nomes_muito_grandes(["Joao", "Constantinos"]) == ["Constantinos"], f"Erro no teste básico"
assert nomes_muito_grandes([]) == [], f"Erro no teste com lista vazia"
assert nomes_muito_grandes(["Ana", "Pedro", "Alexandrino"]) == ["Alexandrino"], f"Erro no teste com vários nomes"
assert nomes_muito_grandes(["Alexandrino", "Bernardinos", "Carlos"]) == ["Alexandrino", "Bernardinos"], f"Erro no teste com múltiplos nomes grandes"
assert nomes_muito_grandes(["Maria", "Jose", "Gabrielinos"]) == ["Gabrielinos"], f"Erro no teste com nome grande no final"

print("Todos os testes passam!")
