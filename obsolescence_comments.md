# Comentários sobre Obsolescências

### main.py (Linha 1)
- **Obsolescência detectada:** 'distutils' module is deprecated in Python 3.12. Use 'setuptools' instead.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### main.py (Linha 12)
- **Obsolescência detectada:** The 'print' function is deprecated in Python 3.12. Use 'print' instead.
- **Código atual:**     print("Pacote configurado com sucesso!")
- **Sugestão:**     print("Pacote configurado com sucesso!")


### teste.py (Linha 1)
- **Obsolescência detectada:** O módulo 'distutils.core' está obsoleto em Python 3.12. Use 'setuptools' em vez disso.
- **Código atual:** from distutils.core import setup
- **Sugestão:** from setuptools import setup


### teste.py (Linha 14)
- **Obsolescência detectada:** A função 'print' agora é uma função, não uma declaração, e não retorna um valor em Python 3.12. Use a função 'print' com o argumento 'file=sys.stderr' para garantir que a saída seja enviada para o fluxo de erro padrão.
- **Código atual:** print("Pacote configurado com sucesso!")
- **Sugestão:** print("Pacote configurado com sucesso!", file=sys.stderr)

