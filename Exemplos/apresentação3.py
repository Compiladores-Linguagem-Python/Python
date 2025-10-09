# Exemplos de código utilizados na terceira apresentação da linguagem Python.

# DECLARAÇÃO E CHAMADA
def saudacao(nome):
    print("Ola,", nome)
saudacao("Cindy")

def soma(a, b):
    return a + b

# PASSAGEM DE PARÂMETROS POR VALOR
def alterar(x):
    x = 10
    print("Dentro da função:", x)
a = 5
alterar(a)
print("Fora da função:", a)

# PASSAGEM DE PARÂMETROS POR REFERÊNCIA
def adicionar(lista):
    lista.append(4)
nums = [1, 2, 3]
adicionar(nums)
print(nums)

# PASSAGEM DE PARÂMETROS POR VALOR-RESULTADO
procedure soma(var x: integer; y: integer); begin  
x := x + y; end;

# PASSAGEM DE PARÂMETROS POR NOME
procedure imprime_duas_vezes(x)  
begin  
    print(x);  
    print(x);  
end;  
integer a := 5;  
imprime_duas_vezes(a + 1);

# CO-ROTINAS
def contagem():
    for i in range(3):
        yield i
for numero in contagem():
    print(numero)

# SUBPROGRAMAS DELEGADOS
def saudacao():
    print("Oi, pessoal!")
mensagem = saudacao
mensagem()

# FUNÇÕES LAMBDA
dobrar = lambda x: x * 2
print(dobrar(5))

# PROGRAMAÇÃO GENÉRICA
def mostrar(item):
    print(item)
mostrar(10)
mostrar("Cindy")
mostrar([1,2,3])


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
    
# DELEGAÇÃO DE EXCEÇÃO
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisão por zero!")
    return a / b
try:
    dividir(5, 0)
except ZeroDivisionError as e:
    print("Erro tratado:", e)
