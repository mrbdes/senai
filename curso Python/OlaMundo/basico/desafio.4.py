# crie um programa que verifique qual a condiçãp do aluno
# relação a sua promoção escolar
# nota >= 70   / APROVADO
# nota >= 40 e nota < 70    / EXAME
# nota  < 40    / REPROVADO
# frequencia > 75  / aprovado ou exame


aluno = int(input("Digite sua nota"))
frequencia = int(input("Digite sua frequencia"))


if aluno < 0 or aluno > 100 or frequencia < 0 or frequencia > 100:
    print("nota e/ou frequencia invalida")
else:
    if aluno >= 70 and frequencia >= 75:
        print("Voce esta aprovado")

    elif aluno >= 40 and aluno < 70 and frequencia <= 75:
        print("voce esta de exame")
    else:
        print("voce esta reprovado")
