# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto. Utilize 'setuptools' para gerenciar pacotes Python.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### main.py (Linha 10)
- **Obsolescência detectada:** Para pacotes com estrutura de diretório específica, é necessário especificar o diretório do pacote. Utilize 'package_dir' para mapear o diretório raiz do pacote.
- **Código atual:** packages=['meu_modulo']
- **Sugestão:** packages=['meu_modulo'], package_dir={'': 'meu_modulo'}


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto. Utilize 'setuptools' para gerenciar pacotes Python.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### teste.py (Linha 6)
- **Obsolescência detectada:** A partir do Python 3.6, é recomendável especificar a versão mínima do Python para o pacote. Isso garante que o pacote seja compatível com a versão correta do Python.
- **Código atual:** setup(
- **Sugestão:** setup(
    python_requires='>=3.6',
    

