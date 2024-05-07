print("-"*80)
print("\n Minha conta \n")
print("-"*80)

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
qnt_dia = 0
limite = 500
max_saque = 3

while True:

    resp = input(menu)

    if resp == "1":
        print("Você escolheu: depósito")
        print(f"Seu saldo atual é de R${saldo:.2f}")
        depositar = float(input("Quanto deseja depositar? \n :"))
        while depositar <= 0: #verifica se o deposito é válido
            print("Valor inválido. Tente novamente.")
            depositar = float(input("Quanto deseja depositar? \n :"))
        saldo +=  depositar
        print(f"Seu saldo atual é de R${saldo:.2f}")

    elif resp == "2":
        print("Você escolheu: saque")
        print("Os saques podem ser realizados 3 vezes ao dia, com limite máximo de R$500,00")
        print(f"Seu saldo atual é de R${saldo}")
        valor = float(input("Quanto deseja sacar? \n :")) 

        if qnt_dia == 3:
            print("Você já realizou o número máximo de saques hoje.")

        elif valor > 500: #verifica se o valor do saque é válido
            print("Valor inválido.")

        elif valor > saldo: 
            print("Você não tem saldo suficiente para realizar essa operção")

        elif valor > 0:
            qnt_dia += 1
            saldo -= valor
            print(f"Foi realizado um saque no valor de {valor}")
            print(f"Você já realizou {qnt_dia}/3 saques disponiveis hoje")
            print(f"Seu saldo atual é de R${saldo}")

        else: 
            print("Valor inválido.")

    elif resp == "3":
        print("Você escolheu: Extrato")
        print(f"Seu saldo atual é de R${saldo:.2f}")

    elif resp == "4":
        print("Você escolheu: Sair")
        print("\n" + "-"*80 + "\n Fim.")
        break

    else:
        print("Opção inválida, tente novamente.")