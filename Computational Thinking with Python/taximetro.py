tarifa_base = 4.5
preco_km = 8
preco_hora_parada=15

km_rodado = float(input("Quantos km rodou?:"))
horas_paradas = float(input("Quanto tempo ficou Parado?:"))

preco_corrrida = tarifa_base+ (preco_km*km_rodado) + (horas_paradas+preco_hora_parada)
print("Sua Corrida ira custar", preco_corrrida)