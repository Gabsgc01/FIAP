a = float(input("insira o valor de a:"))
b = float(input("insira o valor de b:"))
c = float(input("Insira o valor de c:"))
 
delta = (b**2 - 4*a*c)

print("o delta é",delta)

baskara1 = (-b + delta**0.5)/(2*a)
baskara2 = (-b - delta**0.5)/(2*a)

print(f"Baskara1:{baskara1:.2f}")
print(f"Baskara2:{baskara2:.2f}")