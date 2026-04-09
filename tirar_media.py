nome = str(input("Informe o nome do aluno : "))
nota1 = float(input("Digite a primeira nota : "))
nota2 = float(input("Digite a segunda nota : "))
nota3 = float(input("Digite a terceira nota  :"))
media = (nota1 + nota2 + nota3)/3
print(f"Sua média é : {media} ")

if media >=7:
    print("Aluno aprovado")
elif media >= 5 < 7:
    print("Aluno em recuperação")  
elif media <5:
    print('Aluno reprovado')      