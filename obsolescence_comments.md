# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' foi depreciado em favor de 'setuptools'. A versão 3.12 do Python 3.12 não inclui 'distutils' e a função 'setup' agora está disponível em 'setuptools'
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### main.py (Linha 11)
- **Obsolescência detectada:** O módulo 'distutils.core' foi depreciado em favor de 'setuptools'. A versão 3.12 do Python 3.12 não inclui 'distutils' e a função 'setup' agora está disponível em 'setuptools'
- **Código atual:** description='Um exemplo de pacote usando distutils'
- **Sugestão:** description='Um exemplo de pacote usando setuptools'


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' foi depreciado em favor do 'setuptools' no Python 3.12. Use 'setuptools' para criar seus pacotes.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup

