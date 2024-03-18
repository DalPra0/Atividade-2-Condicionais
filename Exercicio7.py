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

##Comece com uma entrada onde o usuário fornece a idade e o peso.
##Em seguida, temos um losango representando uma decisão com duas opções: idade maior que 15 anos e peso inferior ou igual a 120 kg.
##e a idade for maior que 15 anos e o peso for inferior ou igual a 120 kg, o visitante está liberado para andar na montanha russa.
##Se não, o visitante não está liberado para andar na montanha russa.
##A saída é exibida na tela com a mensagem correspondente.
