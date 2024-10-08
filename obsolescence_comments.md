# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto em Python 3.12. Utilize 'setuptools' para configurar pacotes.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### main.py (Linha 8)
- **Obsolescência detectada:** Para a criação de pacotes, o 'distutils' exige o uso de 'package_dir' para indicar a localização do pacote.
- **Código atual:** packages=['meu_modulo']
- **Sugestão:** packages=['meu_modulo'], package_dir={'': 'meu_modulo'}


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto em Python 3.12. Use 'setuptools' em seu lugar.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### teste.py (Linha 6)
- **Obsolescência detectada:** A chamada 'setup' em Python 3.12 requer o argumento 'packages' e 'install_requires' para definir as dependências do pacote.
- **Código atual:**     setup(
- **Sugestão:**     setup(
        packages=find_packages(),
        install_requires=[],
    )

