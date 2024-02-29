import requests

def get_cotacao(destino = 'BRL'):
    
    url = 'https://v6.exchangerate-api.com/v6/fef5402eb8ba5bd668c4dbd2/latest/' + destino

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:

        return data["conversion_rates"]

    else:
        print('Erro ao obter cotações', response.status_code)
        return None

def converter_cotacao(origem = 'USD', destino = 'BRL', valor = 1):
    rates = get_cotacao(destino)
    return round(valor / rates[origem], 2)