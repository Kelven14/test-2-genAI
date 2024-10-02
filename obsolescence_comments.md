# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** 'distutils' module is deprecated in Python 3.12 and will be removed in future versions. Use 'setuptools' instead.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### main.py (Linha 11)
- **Obsolescência detectada:** 'distutils' module is deprecated in Python 3.12 and will be removed in future versions. Use 'setuptools' instead.
- **Código atual:** description='Um exemplo de pacote usando distutils'
- **Sugestão:** description='Um exemplo de pacote usando setuptools'


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto, use 'setuptools' em vez disso.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### teste.py (Linha 10)
- **Obsolescência detectada:** O argumento 'packages' deve ser seguido por uma vírgula, pois é um argumento nomeado.
- **Código atual:** packages=['meu_modulo']
- **Sugestão:** packages=['meu_modulo'],

