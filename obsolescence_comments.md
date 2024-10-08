# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto em Python 3.12. Utilize 'setuptools' para gerenciar pacotes.
- **Código atual:** `from distutils.core import setup`
- **Sugestão:** `from setuptools import setup`


### main.py (Linha 4)
- **Obsolescência detectada:** É recomendável definir a versão mínima do Python para o pacote com 'python_requires' para evitar problemas de compatibilidade.
- **Código atual:** `    setup(`
- **Sugestão:** `    setup(
        python_requires='>=3.6',
        `


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' foi obsoleto e substituído por 'setuptools'. O 'setuptools' oferece mais recursos e suporte para pacotes Python modernos.
- **Código atual:** `from distutils.core import setup`
- **Sugestão:** `from setuptools import setup`


### teste.py (Linha 11)
- **Obsolescência detectada:** Em Python 3.12, a configuração de pacotes com 'packages' requer o uso de 'package_dir' para indicar o diretório raiz dos pacotes.
- **Código atual:** `packages=['meu_modulo']`
- **Sugestão:** `packages=['meu_modulo'],
    package_dir={'': 'meu_modulo'}`

