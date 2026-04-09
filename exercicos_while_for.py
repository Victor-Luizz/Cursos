#Opção de cardápio.
"""""
opcao = 0
while opcao !=4:
    print("\n Olá seja bem vindo ao golaço burguer")
    print("1- x-BURGUER")
    print("2- X -SALADA")
    print("3- x-tudo")
    print("4- batata frita média")
    print("5- encerrar o atendimento")
    opcao = int(input("Escolha uma opção : "))
    if opcao == 1:
        print("Otima escolha ! ")

    elif opcao == 2:
        print("Você escolheu x salada")

    elif opcao ==3:
        print("X tudo")

    elif opcao ==4:
        print("Otima escolha")

    elif opcao == 5 :
        print("Encerrando...")
        break

    else:
        print("opçaõ invalida")                    

   """""     
"""""
texto = ""
while texto.lower () !="sair":
    texto = str(input("Digite um texto ( ou escreva sair para encerrar o programa) : "))
    """""
for num in range (1,13):
    quadrado = num * num  
    print(f" O quadrado de {num} é : {quadrado}")