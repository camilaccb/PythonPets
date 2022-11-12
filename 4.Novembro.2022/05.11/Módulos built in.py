# built in é aquilo que já vem com o python
    # O que já está instalado e o que precisa ser importado
# módulos comuns 
    # math 
    # statistics
    # os
    # pathlib
    # randon 
    # sqlite3
# O script são linhas de código que executam 
# O módulo é um arquivo py que contém várias funções
    # A função que está no módulo precisa ser chamada
    # É possível importar o módulo todo 
        # Cada função do módulo ocupa um espaço na memória 
# Um conjunto de módulos é um pacote 
# Qual a diferença entre módulo e script 
# colocar um conjunto de modulos dentro de uma pasta -> a pasta vira um pacote
    # from pacote.modulo import (nome da definição que vai ser utilizada)

import random 

valor_aleatorio = random.randint(1,5)

from random import randint

valor_aleatorio = randint(1,5)

