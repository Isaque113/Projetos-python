user_name = input("Digite seu nome: ")
user_eage = input("Digite sua idade: ")
inverted_name = f"{user_name[::-1]}"
if user_name and user_eage:
    print(f"Seu nome é {user_name}.")
    print(f"Seu nome invertido é {inverted_name}.")
    if " " in user_name:
        print("Seu nome tem espaços.")
    else:
        print("Seu nome não tem espaços.")
    print(f"Seu nome contem {len(user_name)} letras.")
    print(f"A primeira letra do seu nome é {user_name[:1:]}.")
    print(f"A ultima letra do seu nome é {user_name[:-2:-1]}.")
    print(f"Você tem {user_eage} anos.")
else:
    print("Desculpe, você deixou espaços vazios.")