def carta_mais_forte(carta1: str, carta2: str) -> str:

    if carta1 == carta2:
        return 'iguais'
    
    if carta1 == 'A' and carta2 == '9':
        return 'carta 1'
    if carta2 == 'A' and carta1 == '9':
        return 'carta 2'
    
    if carta1 == 'A':
        return 'carta 2'
    if carta2 == 'A':
        return 'carta 1'
    
    if int(carta1) > int(carta2):
        return 'carta 1'
    else:
        return 'carta 2'

assert carta_mais_forte('2', '3') == 'carta 2', "Três deve ser maior que Dois"
assert carta_mais_forte('9', '9') == 'iguais', "Dois 9 devem ser iguais"
assert carta_mais_forte('7', '8') == 'carta 2', "8 deve ser maior que 7"
assert carta_mais_forte('2', '5') == 'carta 2', "5 é maior que 2"

assert carta_mais_forte('A', '9') == 'carta 1', "Ás deve ser maior que 9"
assert carta_mais_forte('A', '2') == 'carta 2', "Ás deve ser menor que 2"
