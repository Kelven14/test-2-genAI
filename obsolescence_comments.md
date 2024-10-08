# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto em Python 3.12. Use 'setuptools' em vez disso.
- **Código atual:** `from distutils.core import setup`
- **Sugestão:** `from setuptools import setup`


### main.py (Linha 10)
- **Obsolescência detectada:** A sintaxe 'packages' em 'setup' está obsoleta e pode causar problemas de importação. Use 'package_dir' para indicar o diretório raiz do pacote.
- **Código atual:** `packages=['meu_modulo']`
- **Sugestão:** `packages=['meu_modulo'],  package_dir={'': 'meu_modulo'}`


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto no Python 3.12. Use 'setuptools' em vez disso.
- **Código atual:** `from distutils.core import setup`
- **Sugestão:** `from setuptools import setup`


### teste.py (Linha 6)
- **Obsolescência detectada:** Para garantir a compatibilidade com Python 3.12, adicione 'python_requires' ao seu arquivo setup.py. Isso garante que seu pacote seja instalado apenas em versões compatíveis do Python.
- **Código atual:** `    setup(`
- **Sugestão:** `    setup(  
        python_requires='>=3.6',  
        `

