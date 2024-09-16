menu = """

Digite o número da operação solicitada:

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair   

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Digite o valor a ser depositado: "))
        
        if valor <= 0:
            print("Valor inválido para saque, efetue novamente a operação")

        else:
            saldo += valor
            extrato += f"Operação de depósito: R${valor:.2f}\n"
            print(f"Depósito efetuado com sucesso. Novo saldo: R${saldo:.2f}")

    elif opcao == 2:
        valor = float(input("Digite o valor a ser sacado: "))

        if valor > saldo:
            print(f"Valor informado execede o saldo bancário. Saldo {saldo:.2f}")
        
        elif valor > limite:
            print("Valor informado execede o limite(R$ 500,00) de valor por saque.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Limite de quantidade 3 saques diários alcançados, não será possível realizar a operação")
        
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Operação de saque: -R${valor:.2f}\n"
            print(f"Saque efetuado com sucesso. Novo saldo: R${saldo:.2f}")
        
        else:
            print("Valor inválido para saque. Efetue novamente a operação")
 

    elif opcao == 3:
        print("########### EXTRATO ###########")
        print("Não foram realizadas operações" if not extrato else extrato)
        print(f"Saldo disponível: R${saldo:.2f}")
        print("########### EXTRATO ###########")
     
    elif opcao == 4:
        break

    else:
        print("Operação inválida, selecione novamente a operação desejada")