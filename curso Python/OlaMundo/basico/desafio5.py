# Peça ao usuário para inserir um nome de usuário e uma senha.
# Verifique se o nome de usuário é "admin" e a senha é "admin123".
# Exiba uma mensagem de boas-vindas se as credenciais estiverem
# corretas, caso contrário, exiba uma mensagem de erro.
LOGIN_ADMIN = "admin"
SENHA_ADMIN = "admin123"

usuario = input("digite seu login ")
senha = input("Digite sua senha ")

if usuario == ("admin") and senha == ("adimin123"):
    print("ola seja bem vindo!!!")
else:
    if usuario != ("admin") and senha != ("adimin123"):
        print("Erro login")
