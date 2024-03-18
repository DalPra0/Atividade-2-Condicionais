print("")
print("LUCAS DAL PRA BRASCHER - 1C - Atividade 2: Condicionais")
print("")

def avaliar_temperatura(temp):
    if temp < 15:
        return "Está frio!"
    elif temp > 25:
        return "Está calor!"
    else:
        return "Temperatura agradável!"

# Solicita a temperatura do usuário
temperatura = float(input("Digite a temperatura do dia de hoje (em ºC): "))

# Avalia a temperatura e imprime a mensagem correspondente
print(avaliar_temperatura(temperatura))
