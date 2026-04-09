login = str(input("Informe login : "))
senha = int(input("Informe a senha : "))
if login == "victor" and senha == 1234:
    print("Acesso permitido")
elif senha != 1234:
    print("Senha incorreta")

else:
    print("Acesso negado")

