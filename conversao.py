from moedas import converter_cotacao

def menu():
    print()
    print('1 - Converter Dólar em Real')
    print('2 - Converter Euro em Real')
    print('3 - Converter Libras em Real')
    print('4 - Outra cotação')
    print('0 - Sair')
    print()

opcao = 1
while opcao != 0:
    menu()
    opcao = int(input("Escolha uma opção: "))

    destino = 'BRL'
    valor = int(input('Digite o valor: '))

    match opcao:
        case 1: origem = 'USD'
        case 2: origem = 'EUR'
        case 3: origem = 'GBP'
        case 4: 
            origem = input("Digite a Origem: ")
            destino = input("Digite o Destino: ")
    
    if opcao:
        print()
        print('*****************')
        print(f'{origem} para BRL', converter_cotacao(origem, destino, valor))
        print('*****************')
        print()