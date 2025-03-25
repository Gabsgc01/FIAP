segundos= int(input("quantos segundos passaram?:"))

calculo_horas = segundos//3600
calculo_segundos = segundos % 3600
calculo_minutos= segundos//60
calculo_segundos = segundos %60

print(f"passou: {calculo_horas:.2f}, Horas")

print(f"passou:{calculo_minutos:.2f}, Minutos")
print(f"passou:{calculo_segundos:.2f}, Minutos")

