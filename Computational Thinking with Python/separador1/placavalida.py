def placa_valida(placa: str) -> bool:
    if len(placa) != 8:
        return False

    if not (placa[0].isalpha() and placa[1].isalpha() and placa[2].isalpha()):
        return False

    if placa[3] != '-':
        return False

    if not (placa[4].isdigit() and placa[5].isalpha() and placa[6].isdigit() and placa[7].isdigit()):
        return False

    return True


assert placa_valida("ABC-1D23") == True, "Placa válida"
assert placa_valida("XYZ-9Z99") == True, "Outra placa válida"
assert placa_valida("ABCD1D23") == False, "Mais de 3 letras"
assert placa_valida("ABC-DD23") == False, "Quarta posição não é dígito"
assert placa_valida("ABC-1DD2") == False, "Menos de 2 dígitos no final"
assert placa_valida("AB-1D234") == False, "Mais de 2 dígitos no final"
assert placa_valida("ABC-1D234") == False, "Tamanho incorreto"
