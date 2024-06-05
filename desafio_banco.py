# Menu de opções para o usuário
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

# Variáveis para controlar o saldo, limite, extrato e número de saques
saldo = 0  # Saldo inicial da conta
limite = 500  # Limite máximo para cada saque
extrato = ""  # Registro das operações realizadas
numero_saques = 0  # Contador de saques realizados
LIMITE_SAQUES = 3  # Limite máximo de saques permitidos por dia

# Loop principal do programa
while True:
    opcao = input(menu).lower()  # Solicita a opção do usuário e converte para minúsculas

    # Depósito
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))  # Solicita o valor do depósito
        if valor > 0:
            saldo += valor  # Adiciona o valor ao saldo
            extrato += f"Depósito: R$ {valor:.2f}\n"  # Registra o depósito no extrato
        else:
            print("Operação falhou! O valor informado é inválido.")  # Mensagem de erro para valores inválidos

    # Saque
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))  # Solicita o valor do saque
        excedeu_saldo = valor > saldo  # Verifica se o valor do saque é maior que o saldo
        excedeu_limite = valor > limite  # Verifica se o valor do saque excede o limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES  # Verifica se o número de saques excedeu o limite diário

        # Verificações para permitir ou bloquear o saque
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")  # Mensagem de erro para saldo insuficiente
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")  # Mensagem de erro para saque acima do limite
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")  # Mensagem de erro para limite de saques excedido
        elif valor > 0:
            saldo -= valor  # Deduz o valor do saque do saldo
            extrato += f"Saque: R$ {valor:.2f}\n"  # Registra o saque no extrato
            numero_saques += 1  # Incrementa o contador de saques
        else:
            print("Operação falhou! O valor informado é inválido.")  # Mensagem de erro para valores inválidos

    # Exibir extrato
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)  # Verifica se houve movimentações
        print(f"\nSaldo: R$ {saldo:.2f}")  # Exibe o saldo atual
        print("==========================================")

    # Sair do programa
    elif opcao == "q":
        break  # Sai do loop e termina o programa

    # Opção inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")  # Mensagem de erro para opção inválida
