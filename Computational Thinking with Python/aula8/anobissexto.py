def eh_ano_bissexto(ano):
    if (ano % 400 == 0):
        return True
    if (ano % 100 == 0):
        return False
    if (ano % 4 == 0):
        return True
    return False

assert eh_ano_bissexto(2000) == True, "Erro no teste do ano 2000"
assert eh_ano_bissexto(1900) == False, "Erro no teste do ano 1900"
assert eh_ano_bissexto(2024) == True, "Erro no teste do ano 2024"
assert eh_ano_bissexto(2023) == False, "Erro no teste do ano 2023"
assert eh_ano_bissexto(2004) == True, "Erro no teste do ano 2004"

def proximos_cinco_anos_bissextos(ano_atual):
    resultados = []
    ano = ano_atual + 1
    while len(resultados) < 5:
        if eh_ano_bissexto(ano):
            resultados.append(ano)
        ano += 1
    return resultados

assert
