print("")
print("LUCAS DAL PRA BRASCHER - 1C - Atividade 2: Condicionais")
print("")

def verificar_acesso_hopihari(idade, peso):
    if idade > 15 and peso <= 120:
        return "Você está liberado para andar na montanha russa do Hopi Hari!"
    else:
        return "Desculpe, você não está liberado para andar na montanha russa do Hopi Hari."

# Solicita a idade e o peso ao usuário
idade = int(input("Digite sua idade (em anos): "))
peso = float(input("Digite seu peso (em kg): "))

# Verifica se o visitante está liberado para andar na montanha russa
print(verificar_acesso_hopihari(idade, peso))
