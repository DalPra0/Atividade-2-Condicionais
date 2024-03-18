print("")
print("LUCAS DAL PRA BRASCHER - 1C - Atividade 2: Condicionais")
print("")

def calcular_peso_ideal(altura, sexo):
    if sexo.lower() == "masculino" or sexo.lower() == "m":
        peso_ideal = (72.7 * altura) - 58
    elif sexo.lower() == "feminino" or sexo.lower() == "f":
        peso_ideal = (62.1 * altura) - 44.7
    else:
        return "Sexo inválido! Por favor, insira 'masculino' ou 'feminino'."
    
    return f"O peso ideal para uma pessoa do sexo {sexo} com altura {altura}m é {peso_ideal:.2f}kg."

# Solicita altura e sexo do usuário
altura = float(input("Digite a altura da pessoa (em metros): "))
sexo = input("Digite o sexo da pessoa (masculino/feminino): ")

# Calcula e imprime o peso ideal
print(calcular_peso_ideal(altura, sexo))
