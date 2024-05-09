class Bank_account:
    def __init__(self, balance = 0):
        self.__balance = balance
        self.__file = "project/files/transactions.txt"
        self.__transactions = []
        self.__load_transactions()

    def check_statement(self):
        print("==== EXTRATO ====")
        
        for transaction in self.__transactions:
            print(f"{transaction[0]}: {transaction[1]}")

        print("=================")

        print(f"Saldo (=): {self.__balance}")

        print("=================")

    def __load_transactions(self):
        try:
            with open(self.__file, "r") as file:
                for line in file:
                    transaction, amount = line.strip().split(", ")
                    amount = float(amount)

                    self.__transactions.append((transaction, amount))

                if transaction == "Deposito (+)":
                    self.__balance += amount
                elif transaction == "Saque (-)":
                    self.__balance -= amount
        except:
            print("algo deu errado em abrir o arquivo!")
            pass

    def deposit (self, amount):
        self.__balance += amount
        try:
            with open(self.__file, "a") as file:
                file.write(f"Deposito (+), {amount}\n")
                self.__load_transactions()
        except:
            print("Algo deu errado em abrir o arquivo!")
            pass

        print(f"Depósito de R${amount} realizado!")

    def withdraw (self, amount):
        if amount == 0:
            return print("O saque edeveser maior que R$0!")
        if amount <= self.__balance:
            self.__balance -= amount

            try:
                with open(self.__file, "a") as file:
                    file.write(f"Saque (-), {amount}\n")
                    self.__load_transactions()
            except:
                print("Algo deu errado em abrir o arquivo!")
                pass

            print(f"Saque de R${amount} foi realizado!")
        else:
            print("Saldo insuficiente!")
account = Bank_account()

waiting_menu = False # flag
while True:
    if waiting_menu == True:
        input("\nPressione Enter para voltar ao menu...")

    # print("\033[H\033[J") # terminal clear
    print("\033c", end="") # terminal clear
    waiting_menu = True
    
    print('''
=== Automated Teller Machine ===
    [1] Ver extrato
    [2] Fazer Depósito
    [3] Fazer Saque
    [4] Sair
================================
''')

    option = input("\bEscolha uma opção: ")
    print("")

    print(option)

    if option == "1":
        account.check_statement()
    elif option == "2":
        amount = float(input("Digite o valor para depositar: "))
        account.deposit(amount)
    elif option == "3":
        amount = float(input("Digite o valor para sacar: "))
        account.withdraw(amount)
    elif option == "4":
        print("Programa encerrado!\n")
        break
    else:
        print("opção inválida!")