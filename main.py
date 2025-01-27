import os
import time
from colorama import init, Fore, Style
import adicionar_cliente as ac
import listar_cliente as lc
from atualizar_info import atualizar_info as atti
from remover_cliente import remover_cliente as rc

init()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def manner():
    print("-=" * 25)
    
def end_manner():
    print("-=" * 25)
    print()
    
def msg_manner(msg):
    print(msg.center(50, '-'))
    

def menu():
    while True:
        clear_terminal()
        manner()
        incorrect_choice = False
        # opções
        print(Fore.GREEN + "[1] - Adicionar Cliente(s)")
        print("[2] - Listar Cliente(s)")
        print("[3] - Atualizar Info(s)")
        print(Fore.YELLOW + "[4] - Remover Cliente(s)")
        print(Fore.RED + "[5] - SAIR" + Style.RESET_ALL)
        choice = str(input(">."))
        
        # Verifica se o usuário informou um número
        if choice.isnumeric():
            choice = int(choice)
            incorrect_choice = False
        else:
            print(Fore.RED + "Opção Inválida!" + Style.RESET_ALL)
            choice = 0
            incorrect_choice = True
            time.sleep(0.5)
        
            
        if choice == 1:
            ac.adicionar_cliente()
        
        elif choice == 2:
            lc.listar_cliente()
        
        elif choice == 3:
            continuar = ' '
            while continuar != 'n':
                clear_terminal()
                msg_manner("Atualizar informações!")
                print("CAMPOS PARA ATUALIZAR:\nNome, Idade, Endereço, Telefone")
                print()
                nome = input("Nome do Cliente: ")
                campo = input("Campo: ").capitalize()
                if campo == "Idade":
                    nova_info = int(input("Nova informação: "))
                else:
                    nova_info = str(input("Nova informação: "))
                atti(nome, campo, nova_info)
                continuar = input("Deseja atualizar mais informações [S/N]? ").lower()
                if continuar == 'n':
                    break
        
        elif choice == 4:
            rc()
        
        elif choice == 5:
            break
        
        else:
            if not incorrect_choice:
                print(Fore.RED + "Número Inválido!" + Style.RESET_ALL)
                time.sleep(0.5)

    
menu()
msg_manner("FIM!")