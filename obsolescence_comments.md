# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto e deve ser substituído por 'setuptools'
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### main.py (Linha 6)
- **Obsolescência detectada:** O uso de 'packages' é considerado obsoleto e deve ser substituído por 'find_packages' para facilitar a descoberta de pacotes.
- **Código atual:**         packages=['meu_modulo'],
- **Sugestão:**         packages=find_packages(),


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto e foi substituído pelo módulo 'setuptools'. Use 'setuptools' para criar e gerenciar pacotes Python.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### teste.py (Linha 5)
- **Obsolescência detectada:** É recomendado especificar a versão mínima do Python necessária para o projeto. Isso garante que o código seja compatível com as versões mais recentes do Python e evita problemas de compatibilidade.
- **Código atual:**     setup(
- **Sugestão:**     setup(
        python_requires='>=3.6',
        ...

