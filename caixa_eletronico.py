saldo = 1000
extrato = "Extrato Bancario \n"
cont_saque = 0
while True:
    opcao = int(input("""Selecione a opção desejada
    [1] Deposito
    [2] Saque
    [3] Extrato\n"""))
    
    
    
    if opcao == 1: #Depositar
        valor = float(input("Digite a quantidade a ser depositada\n"))    

        if valor <= 0:

            print("Valor Invalido!")
            input("(Pressione qualquer tecla para continuar)")
        else:
            saldo += valor
            extrato += "+ R${} \n".format(valor)
        
            print("""Deposito efetuado com sucesso!
            Saldo atual: R${}""".format(saldo))
            input("(Pressione qualquer tecla para continuar)")
        
    elif opcao == 2: #Sacar
        valor = float(input("Digite a quantidade a ser sacada\n"))
        if valor > saldo:
            print("Saldo Insuficiente.")
            input("(Pressione qualquer tecla para continuar)")
        
        elif valor <= 0:
            print("Valor Invalido!")
            input("(Pressione qualquer tecla para continuar)")
        else:
            if cont_saque < 3 and valor <= 500:
                saldo -= valor
                extrato += "- R${} \n".format(valor)
        
                print("""Saque efetuado com sucesso!
                Saldo atual: R${}""".format(saldo))
                cont_saque += 1
                input("(Pressione qualquer tecla para continuar)")
            elif cont_saque >= 3:
                print("O numero maximo de saques já foi efetuado!")
                input("(Pressione qualquer tecla para continuar)")
            else: 
                print("O valor limite de R$500.00 para saques foi excedido")
                input("(Pressione qualquer tecla para continuar)")

    elif opcao == 3: #Ver Extrato
        if extrato == "Extrato Bancario \n":
            print(extrato)
            print("Não foram realizadas movimentações")
            print("Saldo restante: R${}".format(saldo))
            input("(Pressione qualquer tecla para continuar)")
            
        else:    
            print(extrato)
            print("Saldo restante: R${}".format(saldo))
            input("(Pressione qualquer tecla para continuar)")
            
    else:
        print("Opção invalida")
        input("(Pressione qualquer tecla para continuar)")