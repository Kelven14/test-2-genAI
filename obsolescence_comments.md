# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto. Utilize 'setuptools' para criar e gerenciar pacotes Python.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### main.py (Linha 5)
- **Obsolescência detectada:** A versão do Python 3.6 ou superior é recomendada para usar o módulo 'setuptools'. Adicione a especificação de requisito de Python para garantir a compatibilidade.
- **Código atual:**     setup(
- **Sugestão:**     setup(
        python_requires='>=3.6',
        


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto em Python 3.12 e foi substituído por 'setuptools'.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### teste.py (Linha 10)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto em Python 3.12 e foi substituído por 'setuptools'.
- **Código atual:** description='Um exemplo de pacote usando distutils'
- **Sugestão:** description='Um exemplo de pacote usando setuptools'

