# Primeira parte:
# numero_input = input("Digite um numero inteiro:")
# try:
#     numero_input_int = int(numero_input)
#     if (numero_input_int % 2) == 0:
#         print("É par")
#     elif (numero_input_int % 2) == 1:
#         print("É impar")
# except:
#     print("Esse não é um numero inteiro.")
#     exit()

# Segunda parte:
hora_input = input("Informe as horas:")
try:
    hora_input_int = int(hora_input)
except:
    print("Isso é um texto, reinicie")
    exit()

try:
    if hora_input_int < 0 or hora_input_int == 24:
        print("Não aplicável")
    elif hora_input_int < 12:
        print("Bom dia!")
    elif hora_input_int < 18:
        print("Boa tarde!")
    elif hora_input_int < 24:
        print("Boa noite!")
    else:
        print("Não aplicavel")
except:
    print("Não aplivavel, reinicie.")

# Terceira parte
# primeironome_input = input("Insira seu primeiro nome: ")
# letras_nome = len(primeironome_input)
# if letras_nome  <= 4:
#     print("Seu nome é curto.")
# elif letras_nome > 4 and letras_nome <= 5:
#     print("Seu nome é normal.")
# else:
#     print("Seu nome é muito grande.")