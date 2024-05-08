
conta = (''' 
 --------------------------

 Seja bem-vindo(a)

 O que você deseja fazer?

 [d] Depositar
 [s] Sacar
 [e] Extrato
 [0] Sair

 --------------------------

''')

saldo = 0
extrato = ""
numero_de_saques = 0
limite = 500
LIMITE_SAQUE = 3 


while True:

    opcao = str(input(conta))

    #Depósito
    if opcao == "d":
        depositar = float(input("\n Insira o valor que deseja depositar: \n "))

        if depositar > 0:
            print("\n -> Depósito realizado com sucesso!")
            saldo += depositar
            extrato += f"\n Depósito: R${depositar:.2f}\n"
        
        else:
            print("Operação falhou!")

    #Saque
    elif opcao == "s":
        valor_do_saque = float(input("\n Insira o valor que você deseja sacar: \n "))

        excedeu_saldo = saldo < valor_do_saque
        excedeu_limite = valor_do_saque > limite
        excedeu_saques = numero_de_saques >= LIMITE_SAQUE
         
        if excedeu_saldo:
            print("\n -> Operação falhou! Saldo insuficiente.")

        elif excedeu_limite:
            print("\n -> Operação falhou! Excedeu o valor limite do saque.")

        elif excedeu_saques:
            print("\n -> Operação falhou! Excedeu o número de saques.")
       
        elif valor_do_saque > 0:
            print("\n -> Saque realizado com êxito!")
            saldo -= valor_do_saque
            extrato += f"\n Saque: R${valor_do_saque:.2f}\n"
            numero_de_saques += 1

        else:
            print("\n Operação falhou! Valor inserido inválido.")

        

    #Extrato
    elif opcao == "e":
        print("\n ==============Extrato==============")
        print("\n Não foram realizadas movimentações. \n " if not extrato else extrato)
        print(f"\n -> Saldo: R${saldo:.2f} \n ")
        print("\n ====================================")

    elif opcao == "0":
        break

        

    