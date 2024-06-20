# Classificação de triângulos:
# Peça ao usuário para inserir os comprimentos dos três lados
# de um triângulo e, em seguida, determine se é equilátero
# (todos os lados iguais), isósceles (dois lados iguais)
# ou escaleno (nenhum lado igual).

# triagulo area A + area B + area C

a = float(input('lado A '))
b = float(input('lado B '))
c = float(input('lado C '))

   # Testando se é triângulo
    if a == b and a == c
            print('Equilatero')
     elif  a == b or a == c or b == c:
            print('Isósceles')
    else: a != b or a != c or b !=c: 
            print('Escaleno')
