print("")
print("LUCAS DAL PRA BRASCHER - 1C - Atividade 2: Condicionais")
print("")

def verificar_aprovacao(nota):
    if nota >= 7:
        return "Estudante aprovado"
    elif 4 <= nota < 7:
        return "Estudante em recuperação"
    else:
        return "Estudante reprovado"

# Solicita a nota do estudante
nota = float(input("Digite a nota do estudante: "))

# Avalia a nota e imprime o resultado
print(verificar_aprovacao(nota))
