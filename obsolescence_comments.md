# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto em Python 3.12. Use 'setuptools' em vez disso.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### main.py (Linha 6)
- **Obsolescência detectada:** O formato de versão '0.1dev' está obsoleto. Use '0.1.dev' em vez disso.
- **Código atual:**         version='0.1dev'
- **Sugestão:**         version='0.1.dev'


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto em Python 3.12. Use 'setuptools' para criar pacotes Python.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### teste.py (Linha 7)
- **Obsolescência detectada:** O uso de 'packages' sem 'package_dir' pode levar a problemas com a estrutura do pacote em Python 3.12. É recomendado usar 'package_dir' para definir o diretório raiz do pacote.
- **Código atual:** packages=['meu_modulo']
- **Sugestão:** packages=['meu_modulo'],  package_dir={'': 'meu_modulo'}

