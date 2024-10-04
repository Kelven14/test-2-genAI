# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto em Python 3.12. Use 'setuptools' em vez disso.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### main.py (Linha 10)
- **Obsolescência detectada:** O módulo 'distutils.core' não suporta o argumento 'package_dir', que é necessário para a maioria dos pacotes modernos. Use 'setuptools' em vez disso.
- **Código atual:** packages=['meu_modulo']
- **Sugestão:** packages=['meu_modulo'],  package_dir={'': 'meu_modulo'}


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto, use 'setuptools' em vez disso.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### teste.py (Linha 10)
- **Obsolescência detectada:** Para usar o módulo 'meu_modulo' no pacote 'meu_pacote' você precisa definir o 'package_dir' para que a estrutura do pacote corresponda à estrutura do projeto.
- **Código atual:** packages=['meu_modulo']
- **Sugestão:** packages=['meu_modulo'],  package_dir={'': 'meu_modulo'}

