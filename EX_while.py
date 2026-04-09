#contar quantas pessoas há com mais de 18 anos.
"""""
qtd_pessoas = int(input("Informe quantas pessoas serão adicionadas na conta : "))
contador = 1
maiores = 0
while contador <= qtd_pessoas:
    idade = int(input(f"Digite a idade da pessoa {contador} : "))

    if idade > 18:
        maiores +=1

    contador += 1
print(f"Quantidade de pessoas com mais de 18 anos : {maiores} ")       
"""""

contador = 10  #realiza a conta de forma decrescente.
while contador >=0:
    print(contador)
    contador -=1