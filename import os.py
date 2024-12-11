import os
import sys

# Criar um vetor para armazenar o histórico dos comandos (máximo de 10)
vetor = []

# Simular o terminal
print("Bem-vindo ao terminal do Will")

# Laço de repetição infinito
while True:
    # Comando de entrada
    entrada = input("osh> ")

    # Verifica e executa o último comando com "!!" ou um comando específico "!N"
    if entrada == "!!":
        if vetor:
            entrada = vetor[-1]
            print(f"Executando último comando: {entrada}")
        else:
            print("Nenhum comando no histórico.")
            continue
    elif entrada.startswith("!") and entrada[1:].isdigit():
        index = int(entrada[1:]) - 1
        if 0 <= index < len(vetor):
            entrada = vetor[index]
            print(f"Executando comando histórico: {entrada}")
        else:
            print(f"Comando número {index + 1} não encontrado no histórico.")
            continue

    # Comando para exibir o histórico dos últimos 10 comandos
    elif entrada == "history":
        # Exibir comandos do mais recente ao mais antigo
        for i, cmd in enumerate(reversed(vetor[-10:]), 1):
            print(f"{len(vetor) - (i - 1)} {cmd}")
        continue

    # Criar o processo
    pid = os.fork()
    
    # Verificar se o processo é pai ou filho
    if pid == 0:  # processo filho
        # Separar a entrada em argumentos
        args = entrada.split()
        try:
            # Executar o comando da família exec()
            os.execvp(args[0], args)
        except FileNotFoundError:
            print(f"Comando não encontrado: {args[0]}")
            sys.exit(1)
    elif pid > 0:  # processo pai
        # Esperar o processo filho terminar
        os.wait()
    else:
        print("Houve falha na criação do processo")

    # Armazena o comando no vetor, exceto o comando "exit" e "history"
    if entrada != "exit" and entrada != "history":
        vetor.append(entrada)
        # Limita o histórico a 10 comandos
        if len(vetor) > 10:
            vetor.pop(0)

    # Condição de finalização do terminal
    if entrada == "exit":
        break

print("Adeus usuário, foi bom ter você aqui")
