# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto. Utilize 'setuptools' para criar pacotes Python.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### main.py (Linha 8)
- **Obsolescência detectada:** A opção 'packages' em 'setup' não inclui dependências de pacotes. Utilize 'install_requires' para especificar as dependências necessárias.
- **Código atual:** packages=['meu_modulo']
- **Sugestão:** packages=['meu_modulo'],  install_requires=['meu_modulo']


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto. Use 'setuptools' em vez disso.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### teste.py (Linha 5)
- **Obsolescência detectada:** A versão mínima do Python 3.6 é recomendada para usar o módulo 'setuptools'.
- **Código atual:**     setup(
- **Sugestão:**     setup(
        python_requires='>=3.6',
        

