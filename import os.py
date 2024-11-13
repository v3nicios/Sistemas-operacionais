import os

# Criar um vetor para armazenar os comandos
vetor = []

# Simular o terminal
print("Bem-vindo ao terminal do Will")

# Laço de repeticao infinito
while True:
    # Comando de entrada
    entrada = input("osh> ")

    # Criar o processo
    pid = os.fork();
    # Verificar se o processo é pai ou filho
    if pid == 0: # processo filho
        # Nessa parte é com vcs
        # Executar o comando da família exec()
        print()
    elif pid > 0: # processo pai
        # Vc faz o resto
        print()
    else:
        print("Houve falha na criação do processo")

    # Armazena esses comandos no vetor
    vetor.append(entrada)

    # Condição de finalização do terminal
    if (entrada == "exit"):
        break;

print("Adeus usuário, foi bom ter vc aqui")