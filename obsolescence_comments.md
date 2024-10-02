# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** 'distutils' is deprecated, use 'setuptools' instead.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### main.py (Linha 7)
- **Obsolescência detectada:** The 'packages' argument is deprecated. Use 'py_modules' for single-module packages.
- **Código atual:**         packages=['meu_modulo'],
- **Sugestão:**         py_modules=['meu_modulo'],


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto e foi substituído por 'setuptools'. Para usar o setuptools, importe 'setup' de 'setuptools'.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup

