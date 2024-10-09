# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto. Use 'setuptools' para criar pacotes Python.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### main.py (Linha 6)
- **Obsolescência detectada:** O parâmetro 'packages' com uma lista de strings está obsoleto. Use 'find_packages()' para encontrar automaticamente os pacotes.
- **Código atual:** packages=['meu_modulo'],
- **Sugestão:** packages=find_packages(),


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto em Python 3.12. Use 'setuptools' para criar pacotes Python.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### teste.py (Linha 6)
- **Obsolescência detectada:** O uso de 'packages=['meu_modulo']' é obsoleto. Utilize 'packages=find_packages()' para encontrar automaticamente todos os pacotes em seu projeto.
- **Código atual:**         packages=['meu_modulo'],
- **Sugestão:**         packages=find_packages(),

