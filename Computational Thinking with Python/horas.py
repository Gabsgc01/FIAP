segundos= int(input("quantos segundos passaram?:"))

minutos = segundos//60
segundos = segundos % 60
horas = minutos//60
minutos = minutos%60
segundos = segundos%60

print(f"passaram-se: {horas}hora(s){minutos}minuto(s){segundos}segundo(s)")



