# exemplo_distutils.py

from distutils.core import setup

def main():
    """Função principal que demonstra o uso do distutils."""
    setup(
        name='meu_pacote',
        version='0.1dev',
        packages=['meu_modulo'],
        description='Um exemplo de pacote usando distutils',
        author='Seu Nome',
        author_email='seu.email@example.com',
        url='http://exemplo.com',
    )

    print("Pacote configurado com sucesso!")

if __name__ == "__main__":
    main()
