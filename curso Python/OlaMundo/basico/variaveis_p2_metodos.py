# minha_lista = [1, 2, 3]

# print("Minha lista", minha_lista)

# minha_lista.append(4)

# print("Minha lista", minha_lista)

# minha_lista.insert(1, 33)

# print("Minha lista", minha_lista)


minha_lista = [1, 2, 3, 4, 3, 10, 2, 15, 3]
print("O numero 3 aparece", minha_lista.count(3), "vezes")
print("O numero 2 aparece", minha_lista.count(2), "vezes")


minha_lista.remove(3)
print("minha lista:", minha_lista)


elemento = minha_lista.pop(4)
print("o elemento retirado da minha lista eh", elemento)
print("minha lista:", minha_lista)


meu_dicionario = {
    'nome': 'João',
    'idade': 25,
    'cidade': 'São Paulo',
    'profissao': 'Desenvolvedor',
    'salario': 5000.00,
    'status': 'Empregado',
    'linguagens': ['Python', 'JavaScript', 'C++'],
    'experiencia': {'anos': 3, 'empresa': 'TechCorp'},
    'projetos': {'ativos': 5, 'concluidos': 12},
    'certificacoes': ['Python Developer', 'Web Developer'],
}


# exibindo o dicionario
print(meu_dicionario)
print("quantidade de projetos concluidos",
      meu_dicionario["projetos"]["concluidos"])
print("A primeira certificacao eh:",
      meu_dicionario["certificacoes"][0])
print("minhas chaves", meu_dicionario.keys())
print("OS valores são:", meu_dicionario.values())


# meu_dicionario.clear()
# print(meu_dicionario)

certificacoes = meu_dicionario.pop('certificacoes')
print(certificacoes)
print(meu_dicionario)
