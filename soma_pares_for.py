soma_pares = 0
for s in range(1,11):
    num = int(input(f"Digite p {s} = número : "))
    if num % 2 == 0:
        soma_pares +=num 

print(f"A soma dos números pares é : {soma_pares}")