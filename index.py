from moedas import get_cotacao
from graficos import *

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