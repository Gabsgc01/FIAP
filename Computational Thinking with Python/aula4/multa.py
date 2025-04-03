limite = 50
velocidade = float(input("Qual velocidade o sujeito passou?"))

percentual = ((velocidade - limite)/limite)*100

if percentual <= 20:
    print("R$ 130,16 e 4 pontos na CNH")
elif 20 < percentual <= 50:
    print("R$ 195,23 e 5 pontos na CNH")
elif percentual > 50:
    print("R$ 880,41 e Suspensão da CNH")
else:
    print("Dentro do limite permitido") sad
    
