# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** 'distutils' is deprecated. Use 'setuptools' instead.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### main.py (Linha 10)
- **Obsolescência detectada:** Without 'package_dir', 'setup' will look for 'meu_modulo' in the current directory, which is not expected.
- **Código atual:** packages=['meu_modulo']
- **Sugestão:** packages=['meu_modulo'], package_dir={'': 'meu_modulo'}


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto e foi substituído por 'setuptools'. Use 'setuptools' para criar pacotes Python.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### teste.py (Linha 6)
- **Obsolescência detectada:** O uso de aspas simples para nomes de pacotes está obsoleto. Use aspas duplas para maior clareza e conformidade.
- **Código atual:**         name='meu_pacote',
- **Sugestão:**         name='meu_pacote'

