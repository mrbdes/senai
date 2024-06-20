# as estruturas de decisão ou condicionais em python
# São usadas para tomar decisões com base em condições

# if

idade = int(input("digite sua idade"))

if idade < 18:
    print("Você deve aguardar até as 12h para ir embora!")

else:
    if idade >= 18 and idade < 30:
        print("Seu horario eh as 11h45")
    else:
        print(" voce esta livre")
