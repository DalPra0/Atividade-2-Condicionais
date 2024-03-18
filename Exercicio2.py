import math

print("")
print("LUCAS DAL PRA BRASCHER - 1C - Atividade 2: Condicionais")
print("")

def natureza_das_raizes(a, b, c):
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        return "Existem duas raízes reais distintas."
    elif discriminante == 0:
        return "Existem duas raízes reais iguais."
    else:
        return "Existem duas raízes imaginárias conjugadas."

# Solicita os coeficientes do usuário
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Chama a função para determinar a natureza das raízes e imprime o resultado
print(natureza_das_raizes(a, b, c))
