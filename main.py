valorEmConta = 500
print('Bem-vindo ao caixa eletrônico!')

def menu():
    global valorEmConta  # Declarando a variável como global
    login = input('Login: ')
    password = input('Senha: ')

    if login == 'lincoln' and password == 'estrelinha':
        print('Login realizado com sucesso!')

        while True:
            print('Deseja realizar uma operação de saque, depósito ou sair?')
            escolhaN1 = input('')

            if escolhaN1 == 'saque':
                valorEmConta = saque(valorEmConta)
            elif escolhaN1 == 'deposito':
                valorEmConta = deposito(valorEmConta)
            elif escolhaN1 == 'sair':
                break
            else:
                print('Escolha inválida')

    else:
        print('Senha ou Login incorretos, favor verificar e tentar novamente.')
        menu()  # Chama novamente a função menu em caso de login incorreto

def saque(valor_conta):
    valorSaque = input("Digite o valor que deseja sacar: ")

    if valorSaque.isdigit():
        numero_inteiro = int(valorSaque)
        if numero_inteiro > valor_conta:
            print("Valor digitado não disponível em conta.")
        else:
            valor_conta -= numero_inteiro
            print(f'Sacou {numero_inteiro} reais. Saldo restante: {valor_conta} reais.')
        return valor_conta
    else:
        print(f"{valorSaque} não é um número válido, lembre-se de digitar apenas números.")
        return valor_conta

def deposito(valor_conta):
    valorDeposito = input("Digite o valor que deseja depositar: ")

    if valorDeposito.isdigit():
        numero_inteiro = int(valorDeposito)
        valor_conta += numero_inteiro
        print(f'Depositou {numero_inteiro} reais. Novo saldo: {valor_conta} reais.')
        return valor_conta
    else:
        print(f"{valorDeposito} não é um número válido, lembre-se de digitar apenas números.")
        return valor_conta

menu()