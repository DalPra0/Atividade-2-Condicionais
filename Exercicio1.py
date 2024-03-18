print("")
print("LUCAS DAL PRA BRASCHER - 1C - Atividade 2: Condicionais")
print("")

# Início do programa
x = int(input("Entre com o valor de x: "))  # Leitura do valor de x

# Checagem se x é igual a 0
if x == 0:
    print("Zero")
# Caso x não seja 0, verifica se x é igual a 1
elif x == 1:
    print("Um")
# Caso x não seja 1, verifica se x é igual a 2
elif x == 2:
    print("Dois")
# Se x não for nenhum dos valores acima (0, 1, ou 2)
else:
    print("Erro")