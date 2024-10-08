# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' foi depreciado em favor do 'setuptools'
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### main.py (Linha 11)
- **Obsolescência detectada:** O módulo 'distutils.core' foi depreciado em favor do 'setuptools'
- **Código atual:** description='Um exemplo de pacote usando distutils'
- **Sugestão:** description='Um exemplo de pacote usando setuptools'


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto e deve ser substituído por 'setuptools'.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### teste.py (Linha 8)
- **Obsolescência detectada:** A opção 'packages' em 'setup' não é mais recomendada para módulos únicos. Use 'py_modules' para especificar módulos individuais.
- **Código atual:** packages=['meu_modulo']
- **Sugestão:** packages=['meu_modulo'],  py_modules=['meu_modulo']

