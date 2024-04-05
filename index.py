import time
from datetime import datetime

menu  = """
================================================================

BEM-VINDO AO SISTEMA BANCARIO

    Selecione a operação desejada:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair


================================================================
"""

saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        while True:

            try:

                deposito = float(input("Digite o valor que deseja depositar: "))

                if deposito >= 0:

                    saldo += deposito
                    horario_transacao = datetime.now()
                    extrato += f"TIPO DE OPERACAO: Depósito | VALOR: R$ {deposito} | DATA DA OPERAÇÃO: {horario_transacao} \n"

                    print(f"valor de R$ {deposito} depositado com sucesso!\n"
                          f"Seu saldo agora é de R$ {saldo}\n")

                    time.sleep(2)
                    break
                
                else:
                    print("Erro: O valor inserido é menor que zero, digite novamente.")

                    time.sleep(2)

            except ValueError:
                print("Erro: O valor que voce digitou não é um número, digite novamente.")

                time.sleep(2)

    elif opcao == "s":

        

        while True:

            try:

                saque = float(input("Digite o valor que deseja sacar: "))
                
                
                if saque >= 0:
                    if saque <= limite:
                        if saque <= saldo:

                            if numero_saques < LIMITE_SAQUES:

                                saldo -= saque
                                horario_transacao = datetime.now()
                                extrato += f"TIPO DE OPERACAO: Saque | VALOR: R$ {saque} | DATA DA OPERAÇÃO: {horario_transacao} \n"
                                numero_saques += 1

                                print(f"Saque no valor de R$ {saque} realizado com sucesso! \n"
                                    f"Seu saldo agora é de R$ {saldo}")
                                
                                time.sleep(2)
                                break
                            
                            else:
                                print("Erro: Você atingiu o limite de saques diário!")
                                time.sleep(2)
                                break

                        else:
                            print(f"Não foi possível sacar o valor de R$ {saque}, seu saldo é insuficiente! \n [m] -> voltar ao menu \n [s] -> Tentar novamente \n")

                            opc = input()
                            if opc == "m":
                                break

                            elif opc == "s":
                                continue

                            else:
                                print("Opcao inválida!")
                                time.sleep(2)
                    else:
                        print(f"Erro: O valor digitado está acima do limite de R$ {limite}, Tente novamente!")

                else:
                    print("Erro: O valor inserido é menor que zero, digite novamente!")
                    time.sleep(2)

            except ValueError:

                print("Erro: O valor digitado não é um número. Digite novamente! \n")
                time.sleep(2)   

    elif opcao == "e":
        extrato += f"""================================================================ 
        SALDO ATUAL: R$ {saldo}"""

        print(extrato)

        time.sleep(3)
                    

    elif opcao == "q":
        break

    else:
        print("operacao invalida! Por favor, selecione novamente a operacao desejada.")
        time.sleep(2)

