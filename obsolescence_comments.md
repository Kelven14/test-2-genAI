# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto. Utilize 'setuptools' para a criação de pacotes Python.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### main.py (Linha 7)
- **Obsolescência detectada:** A sintaxe 'packages=['meu_modulo']' está obsoleta. Utilize 'packages=find_packages()' para encontrar automaticamente os pacotes.
- **Código atual:** packages=['meu_modulo']
- **Sugestão:** packages=find_packages()


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto e foi substituído por 'setuptools'. Usar 'setuptools' é recomendado para novas instalações.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### teste.py (Linha 10)
- **Obsolescência detectada:** Para maior clareza e conformidade com as melhores práticas, é recomendado incluir uma licença para o seu pacote.
- **Código atual:** author_email='seu.email@example.com',
- **Sugestão:** author_email='seu.email@example.com',
        license='MIT',

