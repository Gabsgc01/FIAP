def calcular_conta(consumo_kwh, bandeira):
    if bandeira == 'verde':
        preco_kwh = 0.622
    elif bandeira == 'amarela':
        preco_kwh = 0.666
    elif bandeira == 'vermelha1':
        preco_kwh = 0.685
    elif bandeira == 'vermelha2':
        preco_kwh = 0.764

    total = consumo_kwh * preco_kwh
    return round(total, 1) 


assert calcular_conta(100, 'verde') == 62.2
assert calcular_conta(150, 'amarela') == 99.9
assert calcular_conta(200, 'vermelha1') == 137.0
assert calcular_conta(250, 'vermelha2') == 191

print("Todos os testes passaram!")
