print("")
print("LUCAS DAL PRA BRASCHER - 1C - Atividade 2: Condicionais")
print("")

def verificar_aposentadoria(idade, tempo_servico):
    if idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25):
        return "Você pode se aposentar!"
    else:
        return "Você ainda não pode se aposentar."

# Solicita a idade e o tempo de serviço ao usuário
idade = int(input("Digite sua idade (em anos): "))
tempo_servico = int(input("Digite seu tempo de serviço (em anos): "))

# Verifica se o trabalhador pode se aposentar
print(verificar_aposentadoria(idade, tempo_servico))
