# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** 'distutils' is deprecated in Python 3.12. Use 'setuptools' instead.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### main.py (Linha 6)
- **Obsolescência detectada:** 'distutils' does not support 'packages' with nested packages. Use 'package_dir' to specify the root directory of the package.
- **Código atual:**         name='meu_pacote',
- **Sugestão:**         name='meu_pacote',
        package_dir={'': 'meu_modulo'},


### teste.py (Linha 1)
- **Obsolescência detectada:** 'distutils' module is deprecated in Python 3.12, use 'setuptools' instead.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### teste.py (Linha 12)
- **Obsolescência detectada:** The code contains non-ASCII characters. It's recommended to use ASCII characters for better compatibility.
- **Código atual:** print("Pacote configurado com sucesso!")
- **Sugestão:** print("Package configured successfully!")

