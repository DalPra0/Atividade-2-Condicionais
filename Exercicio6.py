print("")
print("LUCAS DAL PRA BRASCHER - 1C - Atividade 2: Condicionais")
print("")

# Inicializa as variáveis P e I
P = []
I = []

# Solicita o número ao usuário
numero = int(input("Digite um número ou 0 para encerrar: "))

while numero != 0:
    # Verifica se o número é par ou ímpar e armazena em P ou I
    if numero % 2 == 0:
        P.append(numero)
    else:
        I.append(numero)
    
    # Solicita outro número ao usuário
    numero = int(input("Digite um número ou 0 para encerrar: "))

# Exibe os valores de P e I
print("Valores pares:", P)
print("Valores impares:", I)