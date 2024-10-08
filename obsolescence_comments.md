# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto. Use 'setuptools' para criar pacotes Python.
- **Código atual:** `from distutils.core import setup`
- **Sugestão:** `from setuptools import setup`


### main.py (Linha 10)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto. Use 'setuptools' para criar pacotes Python.
- **Código atual:** `description='Um exemplo de pacote usando distutils'`
- **Sugestão:** `description='Um exemplo de pacote usando setuptools'`


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' foi depreciado em Python 3.10 e será removido em Python 3.12. Use 'setuptools' como alternativa.
- **Código atual:** `from distutils.core import setup`
- **Sugestão:** `from setuptools import setup`


### teste.py (Linha 11)
- **Obsolescência detectada:** A sintaxe 'author='Seu Nome',' está obsoleta e deve ser substituída por 'author='Seu Nome''.
- **Código atual:** `author='Seu Nome',`
- **Sugestão:** `author='Seu Nome'`

