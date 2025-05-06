import math 

def perto_quad_perfeito(n):
  
    raiz = int(math.sqrt(n))
    
    
    return n == raiz**2 or n == (raiz - 1)**2 or n == (raiz + 1)**2

# Testes
assert perto_quad_perfeito(25) == True   # 5^2
assert perto_quad_perfeito(24) == True   # 5^2 - 1
assert perto_quad_perfeito(26) == True   # 5^2 + 1
assert perto_quad_perfeito(36) == True   # 6^2
assert perto_quad_perfeito(23) == False  # Não está perto de nenhum quadrado perfeito
assert perto_quad_perfeito(16) == True   # 4^2
assert perto_quad_perfeito(17) == True   # 4^2 + 1
assert perto_quad_perfeito(15) == True   # 4^2 - 1
assert perto_quad_perfeito(14) == False  # Não está perto de nenhum quadrado perfeito

print("Passou todos os testes!")