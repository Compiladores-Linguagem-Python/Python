# Exemplos de código utilizados na terceira apresentação da linguagem Python.


# -------------- TRATAMENTO DE EVENTOS E EXCEÇÕES -------------- #


# Tratamento de Eventos Assíncronos

import asyncio

async def tarefa():
    print("Esperando resposta...")
    await asyncio.sleep(2)
    print("Resposta recebida!")

asyncio.run(tarefa())



# Tratamento de Sinais do Sistema

import signal
import sys

def encerrar_programa(sig, frame):
    print("Programa encerrado com segurança")
    sys.exit(0)

signal.signal(signal.SIGINT, encerrar_programa)

print("Programa rodando. Pressione Ctrl+C para sair.")

while True:
    pass



# Tratamento de Exceções

try:
    lista = [1, 2, 3]
    print(lista[5])
except IndexError:
    print("Erro: índice fora da lista!")
else:
    print("Acesso realizado com sucesso!")
finally:
    print("Fim da execução.")



# Criando Exceções Personalizadas

class IdadeInvalida(Exception):
    pass

def verificar_idade(idade):
    if idade < 18:
        raise IdadeInvalida("Menor de idade não permitido!")
    return "Acesso liberado."

try:
    print(verificar_idade(15))
except IdadeInvalida as e:
    print("Erro:", e)