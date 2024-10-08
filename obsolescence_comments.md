# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' foi marcado como obsoleto em Python 3.10. Use 'setuptools' em seu lugar.
- **Código atual:** `from distutils.core import setup`
- **Sugestão:** `from setuptools import setup`


### main.py (Linha 9)
- **Obsolescência detectada:** Em vez de listar os pacotes manualmente, use 'find_packages()' para encontrar automaticamente os pacotes no diretório atual.
- **Código atual:** `packages=['meu_modulo'],`
- **Sugestão:** `packages=find_packages(),`


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto. Use 'setuptools' para criar pacotes Python.
- **Código atual:** `from distutils.core import setup`
- **Sugestão:** `from setuptools import setup`


### teste.py (Linha 11)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto. Use 'setuptools' para criar pacotes Python.
- **Código atual:** `description='Um exemplo de pacote usando distutils'`
- **Sugestão:** `description='Um exemplo de pacote usando setuptools'`

