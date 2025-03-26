segundos= int(input("quantos segundos passaram?:"))

minutos = segundos//60
segundos = segundos % 60
horas = minutos//60
minutos = minutos%60
segundos = segundos%60
dias = horas//24
horas = horas%24

print(f"passaram-se:{dias}dias {horas}hora(s){minutos}minuto(s){segundos}segundo(s)")



