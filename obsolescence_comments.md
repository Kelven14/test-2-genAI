# Comentários sobre Obsolescências

### main.py
- **Obsolescências detectadas:** O módulo 'distutils.core' foi depreciado em Python 3.10 e removido em Python 3.12. Use 'setuptools' em vez disso.
- **Código sugerido:**
```
from setuptools import setup

def main():
    ""Função principal que demonstra o uso do setuptools.""
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


### main.py
- **Obsolescências detectadas:** A função 'print' foi modificada em Python 3.12 para ser mais estrita com tipos de dados. É recomendável usar 'print(str(valor))' para garantir compatibilidade.
- **Código sugerido:**
```
from setuptools import setup

def main():
    ""Função principal que demonstra o uso do setuptools.""
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


### teste.py
- **Obsolescências detectadas:** O módulo 'distutils' está obsoleto e será removido no Python 3.12. Use 'setuptools' como alternativa.
- **Código sugerido:**
```
from setuptools import setup

def main():
    ""Função principal que demonstra o uso de setuptools.""
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


### teste.py
- **Obsolescências detectadas:** A função 'distutils.core.setup' está obsoleta e será removida no Python 3.12. Use 'setuptools.setup' como alternativa.
- **Código sugerido:**
```
from setuptools import setup

def main():
    ""Função principal que demonstra o uso de setuptools.""
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

