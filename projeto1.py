nome = "Isaque"
sobrenome = "Carlos Farias"
idade = int('18')
ano_de_nascimento = 2025 - 1 - idade
maior_de_idade = idade >= 18
altura = float("1.70")
print("Nome completo:", nome, sobrenome)
print('Idade:', idade)
print("Ano de nascimento", ano_de_nascimento)
if maior_de_idade is True:
    print("Maior de idade: Sim")
else:
    print("maior de idade: não")
print("Altura:", altura)