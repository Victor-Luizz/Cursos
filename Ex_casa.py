# Calculo de imc, crie um programa em que peça o peso e altura do cliente.
"""""
peso = int(input("Informe o seu peso : "))
altura = float(input("Informe sua altura : "))
imc = (altura **2) / peso 
print(f"Sua massa corporea é : {imc}")
"""""
#crie um programa em que informe quantas palavras se repetem na frase !
frase = input("Informe a frase : ")
vogais= "aeiou"
contador =0
for letra in frase.lower():
    if letra in vogais:
        contador += 1
        print(f"Quantidade de vogais : {contador}")