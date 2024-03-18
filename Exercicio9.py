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

##Comece com duas entradas onde o usuário fornece a idade e o tempo de serviço.
##Em seguida, temos um losango representando uma decisão com três opções: idade maior ou igual a 65 anos, tempo de serviço maior ou igual a 30 anos e uma combinação de idade maior ou igual a 60 anos e tempo de serviço maior ou igual a 25 anos.
##Se a idade for maior ou igual a 65 anos, o trabalhador pode se aposentar.
##Se o tempo de serviço for maior ou igual a 30 anos, o trabalhador pode se aposentar.
##Se a idade for maior ou igual a 60 anos e o tempo de serviço for maior ou igual a 25 anos, o trabalhador pode se aposentar.
##Se nenhuma das condições acima for atendida, o trabalhador não pode se aposentar.
##A saída é exibida na tela com a mensagem correspondente à possibilidade de aposentadoria.