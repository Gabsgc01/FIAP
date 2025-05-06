def calcular(num1,num2,conta):

    if conta == "+":
        resultado = num1 + num2
        return resultado
    elif conta =="-":
        resultado = num1 - num2
        return resultado
    elif conta =="*":
        resultado = num1 * num2
        return resultado
    elif conta =="/":
        resultado = num1 / num2
        return resultado


assert(calcular(6,2,"+"))== 8
assert(calcular(6,2,"-"))== 4
assert(calcular(6,2,"*"))== 12
assert(calcular(6,2,"/"))== 3


calcular(num1,num2,conta)