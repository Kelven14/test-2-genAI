# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** 'distutils' module is deprecated. Use 'setuptools' instead.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### main.py (Linha 6)
- **Obsolescência detectada:** Python 3.12 requires explicit specification of Python version compatibility using 'python_requires' in 'setup.py'.
- **Código atual:**     setup(
- **Sugestão:**     setup(
        python_requires='>=3.6',
        


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto em Python 3.12. Use 'setuptools' como alternativa.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### teste.py (Linha 5)
- **Obsolescência detectada:** A especificação de requisitos de Python é recomendada para evitar problemas de compatibilidade. Use 'python_requires' para definir a versão mínima do Python necessária.
- **Código atual:**     setup(
- **Sugestão:**     setup(
        python_requires='>=3.6',
        ...

