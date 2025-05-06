def soma_pares(n: int):
    soma = 0
    for i in range(2, n+1, 2):  # Começa de 2 e vai até n (inclusive), pulando de 2 em 2
        soma += i
    return soma


assert(soma_pares(16))
assert(soma_pares(14))
assert(soma_pares(10))
