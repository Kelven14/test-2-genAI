# Comentários sobre Obsolescências

### main.py
- **Obsolescências detectadas:** A biblioteca 'distutils.core' está obsoleta em Python 3.12. Use 'setuptools' para a criação de pacotes., A função 'urllib.urlopen' está obsoleta. Use a biblioteca 'urllib.request' para realizar requisições HTTP., A verificação de SSL desabilitada no 'requests.get' é considerada uma prática insegura. Use 'verify=True' para habilitar a verificação de SSL.
- **Código sugerido:**
```
from setuptools import setup
import urllib.request
import requests

def fetch_data(url):
    # Usando a biblioteca urllib.request
    with urllib.request.urlopen(url) as response:
        return response.read()

def main():
    url = "http://example.com/data"
    
    # Utilizando requests com a verificaÃ§Ã£o de SSL habilitada
    response = requests.get(url, verify=True)
    if response.status_code == 200:
        data = fetch_data(url)
        print("Dados obtidos:", data)
    else:
        print("Erro ao obter dados:", response.status_code)

if __name__ == "__main__":
    setup(
        name='meu_pacote',
        version='0.1dev',
        description='Exemplo de pacote usando setuptools',
        author='Seu Nome',
        author_email='seu.email@example.com',
        url='http://exemplo.com',
    )
    main()
```


### teste.py
- **Obsolescências detectadas:** O módulo 'distutils' está obsoleto no Python 3.12 e foi removido. Utilize 'setuptools' para a criação de pacotes., O módulo 'distutils.core' foi removido. Utilize 'setuptools' para a criação de pacotes.
- **Código sugerido:**
```
from setuptools import setup

def main():
    """Função principal que demonstra o uso do setuptools."""
    setup(
        name='meu_pacote',
        version='0.1dev',
        packages=['meu_modulo'],
        description='Um exemplo de pacote usando setuptools',
        author='Seu Nome',
        author_email='seu.email@example.com',
        url='http://exemplo.com',
    )

    print("Pacote configurado com sucesso!")

if __name__ == "__main__":
    main()
```

