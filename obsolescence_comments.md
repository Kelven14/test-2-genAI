# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto em Python 3.12. Utilize 'setuptools' em seu lugar.
- **Código atual:** `from distutils.core import setup`
- **Sugestão:** `from setuptools import setup`


### main.py (Linha 8)
- **Obsolescência detectada:** O argumento 'packages' do setup() precisa ser acompanhado do argumento 'package_dir' para definir a estrutura do pacote.
- **Código atual:** `packages=['meu_modulo']`
- **Sugestão:** `packages=['meu_modulo'], package_dir={'': 'meu_modulo'}`


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto em Python 3.12. Use 'setuptools' para gerenciar pacotes Python.
- **Código atual:** `from distutils.core import setup`
- **Sugestão:** `from setuptools import setup`


### teste.py (Linha 8)
- **Obsolescência detectada:** Para especificar o diretório raiz do pacote, é necessário usar 'package_dir' em Python 3.12.
- **Código atual:** `packages=['meu_modulo']`
- **Sugestão:** `packages=['meu_modulo'], package_dir={'': 'meu_modulo'}`

