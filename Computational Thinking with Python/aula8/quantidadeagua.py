def avaliar_consumo_agua(consumos_ml):
    total = sum(consumos_ml)
    
    if total < 2000:
        return 'insuficiente'
    elif total <= 3000:
        return 'suficiente'
    else:
        return 'excesso'


print(avaliar_consumo_agua([500, 500]))                       
assert avaliar_consumo_agua([500, 500]) == 'insuficiente'     # 1000ml < 2000ml

# Teste2
print(avaliar_consumo_agua([1000, 1000, 900]))                
assert avaliar_consumo_agua([1000, 1000, 900]) == 'suficiente'  # 2900ml

# Teste3
print(avaliar_consumo_agua([1500, 1500, 1500]))                
assert avaliar_consumo_agua([1500, 1500, 1500]) == 'excesso'    # 4500ml

print("Todos os testes passaram!")
