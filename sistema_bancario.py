import os
import time

menu = """
    ----SISTEMA BANCARIO----
    
         (1) Deposito
         (2) Saque
         (3) Extrato
            
         (0) Sair
"""

saldo = 0
limite = 500
extrato = ""
qtd_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    # Deposito
    if (opcao == 1):
        deposito = float(input("Deposite o valor que deseja: "))

        if (deposito > 0):
            saldo += deposito
            extrato += (f"Deposito: R$ {deposito: .2f}\n")
            print("Deposito efetuado com sucesso!")
            time.sleep(2.5)
            os.system('cls')
        else:
            print("Erro ao depositar! Tente novamente.")
            time.sleep(2.5)
            os.system('cls')

    # Saque
    elif (opcao == 2):

        saque = float(input("Informe a quantia que deseja sacar: "))

        saldo_insuficiente = saque > saldo
        limite_atingido = saque > limite
        limite_saques_diario = qtd_saques > LIMITE_SAQUES

        if (saldo_insuficiente):
            print("Erro ao efetuar saque! Saldo insuficiente.")
            time.sleep(2.5)
            os.system('cls')

        elif (limite_atingido):
            print("Erro ao efetuar saque! Saque deve ser no maximo de R$ 500,00.")
            time.sleep(2.5)
            os.system('cls')

        elif (limite_saques_diario):
            print("Erro ao efetuar saque! Limite de saques diario atingido.")
            time.sleep(2.5)
            os.system('cls')

        elif (saque > 0):
            saldo -= saque
            extrato += (f"Saque: R$ {saque: .2f}\n\n")
            qtd_saques += 1
            print("Saque efetuado com sucesso!")
            time.sleep(2.5)
            os.system('cls')

        else:
            print("Erro ao efetuar saque! O valor informado é invalido.")
            time.sleep(2.5)
            os.system('cls')

    # Extrato
    elif (opcao == 3):

        os.system('cls')
        print("  EXTRATO BANCARIO")
        print("=====================\n")
        print(extrato)
        print(f"\nSaldo Atual: R$ {saldo: .2f}")
        print("=====================\n")

    elif (opcao == 0):
        os.system('cls')
        break

    else:
        print("\nOpção Invalida! Selecione uma das opções.")
        time.sleep(2.5)
        os.system('cls')
