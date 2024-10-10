# Importando bibliotecas obsoletas
from distutils.core import setup
import urllib
import requests

def fetch_data(url):
    # Usando uma função de urllib que foi descontinuada
    response = urllib.urlopen(url)
    return response.read()

def main():
    url = "http://example.com/data"
    
    # Utilizando requests sem a verificação de SSL, que não é recomendada
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        data = fetch_data(url)
        print("Dados obtidos:", data)
    else:
        print("Erro ao obter dados:", response.status_code)

if __name__ == "__main__":
    setup(
        name='meu_pacote',
        version='0.1dev',
        description='Exemplo de pacote usando distutils',
        author='Seu Nome',
        author_email='seu.email@example.com',
        url='http://exemplo.com',
    )
    main()
