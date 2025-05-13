def placa_valida(placa):
    if len(placa) != 8:
        return False
    if not (placa[0].isalpha() and placa[1].isalpha() and placa[2].isalpha()):
        return False
     if placa[3] != '-':
        return False
    if not (placa[4].isdigit() and placa[5].isalpha() and placa[6].isdigit() and placa[7].isdigit()):
        return False
     return True


