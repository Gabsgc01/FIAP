def digito_ou_letra(caractere):
    if caractere.isdigit():
        return 'digito'
    elif caractere.isalpha():
        return 'letra'
    else:
        return 'nenhum'


assert digito_ou_letra('a') == 'letra'
assert digito_ou_letra('z') == 'letra'
assert digito_ou_letra('3') == 'digito'
assert digito_ou_letra('@') == 'nenhum'