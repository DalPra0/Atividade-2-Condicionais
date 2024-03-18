print("")
print("LUCAS DAL PRA BRASCHER - 1C - Atividade 2: Condicionais")
print("")

def verificar_situacao_eleitoral(idade):
    if idade < 16:
        return "Não eleitor"
    elif 16 <= idade < 18 or idade >= 65:
        return "Eleitor facultativo"
    else:
        return "Eleitor obrigatório"

# Solicita a idade ao usuário
idade = int(input("Digite sua idade: "))

# Verifica a situação eleitoral
print("Sua situação eleitoral é:", verificar_situacao_eleitoral(idade))
