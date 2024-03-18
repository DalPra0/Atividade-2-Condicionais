print("")
print("LUCAS DAL PRA BRASCHER - 1C - Atividade 2: Condicionais")
print("")

def verificar_situacao_estudante(nota1, nota2, codigo_universidade):
    media = (nota1 + nota2) / 2

    if codigo_universidade == 1:
        if media >= 7.0:
            return "Aprovado"
        elif 4.0 <= media < 7.0:
            return "Em exame"
        else:
            return "Reprovado"
    elif codigo_universidade == 2:
        if media >= 5.0:
            return "Aprovado"
        else:
            return "Em exame"
    else:
        return "Código de universidade inválido"

# Solicita as notas e o código da universidade ao usuário
nota1 = float(input("Digite a primeira nota bimestral: "))
nota2 = float(input("Digite a segunda nota bimestral: "))
codigo_universidade = int(input("Digite o código da universidade (1 para PUCPR, 2 para UNICAMP): "))

# Verifica a situação do estudante
print("Situação do estudante:", verificar_situacao_estudante(nota1, nota2, codigo_universidade))

##Comece com três entradas onde o usuário fornece a primeira nota, a segunda nota e o código da universidade.
##Em seguida, temos um losango representando uma decisão com duas opções: código da universidade igual a 1 (PUCPR) e código da universidade igual a 2 (UNICAMP).
##Para o código da universidade igual a 1 (PUCPR), verificamos a média e decidimos se o estudante está aprovado, em exame ou reprovado com base nas diretrizes da instituição.
##Para o código da universidade igual a 2 (UNICAMP), verificamos a média e decidimos se o estudante está aprovado ou em exame com base nas diretrizes da instituição.
##A saída é exibida na tela com a situação do estudante.
