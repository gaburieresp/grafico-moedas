import matplotlib.pyplot as plt
from moedas import get_cotacao

cotacoes = get_cotacao()

l_moedas = ['USD - Dólar', 'EUR - Euro', 'GBP - Libras']
l_valores = [1 / cotacoes['USD'], 1 / cotacoes ['EUR'], 1 / cotacoes['GBP']]

def grafico_barra(l_moedas, l_valores):
    plt.bar(l_moedas, l_valores)
    plt.title('Conversões ao Real (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('BRL R$')
    plt.show()

def grafico_pizza(l_moedas, l_valores):
    plt.pie(l_valores, labels= l_moedas)
    plt.title('Proporção em relação ao Real (BRL)')
    plt.show()

def grafico_dispersao(l_moedas, l_valores):
    plt.scatter(l_moedas, l_valores)
    plt.title('Conversões ao Real (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('BRL R$')
    plt.show()

def menu():
    print()
    print('1 - Gráfico de barras')
    print('2 - Gráfico de pizza')
    print('3 - Gráfico de dispersão')
    print('0 - Sair')
    print()

opcao = 1

while opcao != 0:
    menu()
    opcao = int(input('Escolha um tipo de gráfico: '))

    match opcao:
        case 1: grafico_barra(l_moedas, l_valores)
        case 2: grafico_pizza(l_moedas, l_valores)
        case 3: grafico_dispersao(l_moedas, l_valores)

print()
print('Até a próxima!')
