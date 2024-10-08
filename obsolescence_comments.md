# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' foi depreciado. Utilize 'setuptools' para criar pacotes Python.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto em Python 3.12. Use 'setuptools' em vez de 'distutils'.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup

