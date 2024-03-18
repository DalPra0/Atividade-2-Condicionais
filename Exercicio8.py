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

##Comece com uma entrada onde o usuário fornece a idade.
##Em seguida, temos um losango representando uma decisão com três opções: idade menor que 16 anos, idade entre 16 e 18 anos (inclusive) ou idade maior ou igual a 65 anos.
##Se a idade for menor que 16 anos, a pessoa é classificada como "Não eleitor".
##Se a idade estiver entre 16 e 18 anos (inclusive) ou for maior ou igual a 65 anos, a pessoa é classificada como "Eleitor facultativo".
##Se a idade estiver fora dessas faixas, a pessoa é classificada como "Eleitor obrigatório".
##A saída é exibida na tela com a situação eleitoral correspondente.