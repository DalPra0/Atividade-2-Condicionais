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
