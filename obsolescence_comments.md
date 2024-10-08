# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto em Python 3.12. Utilize 'setuptools' para criar pacotes.
- **Código atual:** `from distutils.core import setup`
- **Sugestão:** `from setuptools import setup`


### main.py (Linha 10)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto em Python 3.12. Utilize 'setuptools' para criar pacotes.
- **Código atual:** `description='Um exemplo de pacote usando distutils'`
- **Sugestão:** `description='Um exemplo de pacote usando setuptools'`


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' foi depreciado em favor de 'setuptools'. Utilize 'setuptools' para criar pacotes Python.
- **Código atual:** `from distutils.core import setup`
- **Sugestão:** `from setuptools import setup`


### teste.py (Linha 6)
- **Obsolescência detectada:** O formato de versão '0.1dev' está obsoleto. Utilize o formato semântico de versão, como '0.1.dev', para garantir compatibilidade.
- **Código atual:** `        version='0.1dev'`
- **Sugestão:** `        version='0.1.dev'`

