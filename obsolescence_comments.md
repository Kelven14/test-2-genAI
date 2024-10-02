# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' foi depreciado em Python 3.12. Use 'setuptools' para criar pacotes.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### main.py (Linha 6)
- **Obsolescência detectada:** O argumento 'packages' é considerado obsoleto. Use 'find_packages()' da biblioteca setuptools para encontrar os pacotes automaticamente.
- **Código atual:**     setup(
- **Sugestão:**     setup(
        packages=find_packages(),
    )


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' foi depreciado e 'setuptools' é o recomendado
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### teste.py (Linha 10)
- **Obsolescência detectada:** É recomendável incluir o pacote como requisito para garantir que a instalação seja correta
- **Código atual:** packages=['meu_modulo']
- **Sugestão:** packages=['meu_modulo'],  install_requires=['meu_modulo']

