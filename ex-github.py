#Faça um programa que peça dois números e imprima a soma:
"""""
num1 = int(input("Informe o primeiro número : "))
num2 = int(input("Informe o segundo número : "))
soma = num1 + num2 
print(f"Soma é igual : {soma} ")
"""""
"""""
nota1 = int(input("INFORME A PRIMEIRA NOTA : "))
nota2 = int(input("INFORME A SEGUNDA NOTA : "))
nota3 = int(input("INFORME A TERCEIRA NOTA : "))
nota4 = int(input("INFORME A QUARTA NOTA : "))
media = (nota1 + nota2 + nota3 + nota4) /4
print(media)
"""""
#FAÇA UM PROGRAMA QUE CONVERTA METROS PARA CENTÍMETROS
"""""
metros = float(input("Digite o valor em metros : "))
centimetros =  metros * 100
print(f"{metros} metros equivalem a {centimetros} centimetros.")
"""""
#Faça um programa em que calcule a area de um quadrado em seguida
# mostre o dobro dessa area ao usúario.
"""""
area1 = float(input("INFORME O VALOR DA AREA DO QUADRADO : "))
print(f"A AREA É EQUIVALENTE À : {area1 * 2}")
"""""
#Faça um programa em que pergunte quanto voce por hora e o numero 
# de horas trabalhadas por mes e mostre quanto voce recebe ao total no mes 
"""""
pergunta1 = int(input("QUANTO VOCÊ GANHA POR HORA ? "))
pergunta2 =  int(input("QUANTAS HORAS VOCÊ TRABALHA NO MES ? "))
print(f" O SALÁRIO MENSAL É EQUIVALENTE A : {pergunta1 * pergunta2 }")
"""

#TENDO COMO DADOS DE ENTRADA UM ARQUIVO EM GIGABYTES,
#CONSTRUA UM ALGORÍTMO QUE FAÇA A CONVERSÃO PARA MEGABYTES
#GIGABYTES * 1024
"""""
giga = int(input("Informe quantos gigas há no programa: "))
print(f"EM MEGABYTES FICA : {giga * 1024}")
"""""

giga = int(input("Informe o valor de gigabytes: "))
print(f"em megabytes fica : {giga * 1024}")
print(f"em kilobytes fica : {giga * 1024 * 1024 }")