import os
from Processo import Processo
from Atendimento import Atendimento
from FilaDeProcessos import FilaDeProcessos

os.system("cls")
fila = FilaDeProcessos()
atendidos = Atendimento()

def menuPrincipal():
    return "1 - Cadastrar processo\n2 - Consultar processo\n3 - Listar processos\n4 - Anunciar próximo na fila\n5 - Atender processo\n6 - Consultar atendidos\n0 - Sair\n"
    
    
while True:
    userInput = input(menuPrincipal())
    
    os.system("cls")
    
    if userInput == "1":
        protocolo = input("Digite o protocolo: ")
        nomeInteressado = input("Digite o nome da pessoa interessada: ")
        assunto = input("Digite o assunto: ")
        
        os.system("cls")
        if protocolo and nomeInteressado and assunto:
            if fila.protocoloIsValid(protocolo):
                fila.queue(Processo(protocolo, nomeInteressado, assunto))
                print("Processo criado.\n")
            else:
                print(f"Já existe um processo com o protocolo {protocolo} cadastrado.\n")
        else:
            print("Todos os campos devem ser preenchidos.\n")
            
    elif userInput == "2":
        protocolo = input("Digite o protocolo: ")
        os.system("cls")
        print(fila.findByProtocolo(protocolo))
    
    elif userInput == "3":
        print(fila.toString())
    
    elif userInput == "4":
        print(fila.next())
    
    elif userInput == "5":
        retorno = fila.dequeue()
        if isinstance(retorno, str):
            print(retorno)
        else:
            atendidos.add(retorno)
            print("Processo atendido.\n")
    
    elif userInput == "6":
        print(atendidos.toString())
            
    elif userInput == "0":
        break
    
    else:
        os.system("cls")
        print("Opção Inválida.")