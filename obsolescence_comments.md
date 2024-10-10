# Comentários sobre Obsolescências

### main.py
- **Obsolescências detectadas:** O módulo 'distutils' está obsoleto no Python 3.12 e foi removido. Use 'setuptools' como alternativa., A função 'setup' do módulo 'distutils.core' foi removida. Use a função 'setup' do módulo 'setuptools' como alternativa.
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
- **Obsolescências detectadas:** O módulo 'distutils' está obsoleto em Python 3.12. Use 'setuptools' como alternativa.
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

