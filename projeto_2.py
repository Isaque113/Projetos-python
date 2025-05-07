introdução = "COMPARADOR DE VALORES"
print(introdução)
valor1 = input("Insira o primeiro valor: ")
valor2 = input("Insira o segundo valor: ")

if valor1 > valor2:
    print(f"{valor1} é maior que {valor2}")
elif valor1 < valor2:
    print(f'{valor1} é menor que {valor2}')
elif valor1 == valor2:
    print("os dois valores são iguais")
else:
    print("Não aplicavel")