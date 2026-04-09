tarefas = [] 
tarefas.append("Tomar banho")
tarefas.append("Tomar café")
tarefas.append("Almoçar")
tarefas.append("Reunião com clientes ")
tarefas.append("Ir para academia ")

print("--------- Minhas tarefas ----------- ")
for t in tarefas:
    print(",",t)

print("\n Adicionar mais uma tarefa no dia ! ")
tarefas.append("Ir correr ")
for t in tarefas:
    print(",",t)    

print("Retirar uma tarefa do dia ! ")  
tarefas.remove("Reunião com clientes ") 
for t in tarefas:
    print(",",t) 