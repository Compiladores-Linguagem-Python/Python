"""
Demonstração das Características da Linguagem Python
Este arquivo reúne exemplos dos principais aspectos da linguagem Python.
"""

# =============================================================================
# TIPOS DE DADOS
# =============================================================================

def demonstrar_tipos_dados():
    """Demonstra os tipos de dados primitivos e compostos do Python"""
    print("=" * 60)
    print("TIPOS DE DADOS")
    print("=" * 60)
    
    # Tipos primitivos
    print("\n1. TIPOS PRIMITIVOS:")
    print("-" * 40)
    
    # Inteiros (int) - tamanho variável
    numero_inteiro = 42
    print(f"Inteiro: {numero_inteiro}, tipo: {type(numero_inteiro)}, tamanho: {numero_inteiro.bit_length()} bits")
    
    # Ponto flutuante (float) - 64 bits
    numero_float = 3.14159
    print(f"Float: {numero_float}, tipo: {type(numero_float)}")
    
    # Complexos (complex)
    numero_complexo = 2 + 3j
    print(f"Complexo: {numero_complexo}, tipo: {type(numero_complexo)}")
    
    # Booleanos (bool)
    verdadeiro = True
    falso = False
    print(f"Booleanos: {verdadeiro}, {falso}, tipos: {type(verdadeiro)}, {type(falso)}")
    
    # Strings (str) - Unicode
    texto = "Olá, mundo!"
    print(f"String: {texto}, tipo: {type(texto)}")
    
    # Tipos compostos
    print("\n2. TIPOS COMPOSTOS:")
    print("-" * 40)
    
    # Listas (list) - vetores dinâmicos
    lista = [1, "dois", 3.0, [4, 5]]
    print(f"Lista: {lista}, tipo: {type(lista)}, tamanho: {len(lista)}")
    
    # Tuplas (tuple) - imutáveis
    tupla = (1, "dois", 3.0)
    print(f"Tupla: {tupla}, tipo: {type(tupla)}")
    
    # Dicionários (dict) - pares chave-valor
    dicionario = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
    print(f"Dicionário: {dicionario}, tipo: {type(dicionario)}")
    
    # Conjuntos (set) - elementos únicos
    conjunto = {1, 2, 3, 3, 4}  # Resultará em {1, 2, 3, 4}
    print(f"Conjunto: {conjunto}, tipo: {type(conjunto)}")

# =============================================================================
# REFERÊNCIAS E VARIÁVEIS
# =============================================================================

def demonstrar_referencias_variaveis():
    """Demonstra o uso de referências e características de variáveis"""
    print("\n" + "=" * 60)
    print("REFERÊNCIAS E VARIÁVEIS")
    print("=" * 60)
    
    # Uso de referências
    print("\n1. USO DE REFERÊNCIAS:")
    print("-" * 40)
    
    a = [1, 2, 3]
    b = a  # b referencia o mesmo objeto que a
    b.append(4)
    print(f"a: {a}, b: {b}")  # Ambos serão [1, 2, 3, 4]
    
    # Cópia real
    c = a.copy()
    c.append(5)
    print(f"a: {a}, c: {c}")  # a permanece [1, 2, 3, 4], c será [1, 2, 3, 4, 5]
    
    # Variáveis
    print("\n2. VARIÁVEIS:")
    print("-" * 40)
    
    # Nomes de variáveis (case sensitive)
    variavel_valida = 10
    VARIAVEL_MAIUSCULA = 20
    _variavel_privada = 30
    
    print(f"Variáveis: {variavel_valida}, {VARIAVEL_MAIUSCULA}, {_variavel_privada}")
    
    # Vinculação dinâmica
    x = 10        # x é inteiro
    print(f"x: {x}, tipo: {type(x)}")
    x = "dez"     # agora x é string
    print(f"x: {x}, tipo: {type(x)}")
    
    # Escopo
    print("\n3. ESCOPO DE VARIÁVEIS:")
    print("-" * 40)
    
    variavel_global = "acessível em todo lugar"
    
    def funcao_exemplo():
        variavel_local = "acessível apenas nesta função"
        global variavel_global
        variavel_global = "modificada dentro da função"
        print(f"Dentro da função: {variavel_local}")
    
    funcao_exemplo()
    print(f"Fora da função: {variavel_global}")

# =============================================================================
# EXPRESSÕES E OPERADORES
# =============================================================================

def demonstrar_expressoes():
    """Demonstra expressões, precedência e sobrecarga de operadores"""
    print("\n" + "=" * 60)
    print("EXPRESSÕES E OPERADORES")
    print("=" * 60)
    
    # Precedência de operadores
    print("\n1. PRECEDÊNCIA DE OPERADORES:")
    print("-" * 40)
    
    resultado = 10 + 5 * 2 ** 3  # 5 * 8 = 40, depois 10 + 40 = 50
    print(f"10 + 5 * 2 ** 3 = {resultado}")
    
    # Forçando precedência com parênteses
    resultado2 = (10 + 5) * 2 ** 3  # 15 * 8 = 120
    print(f"(10 + 5) * 2 ** 3 = {resultado2}")
    
    # Sobrecarga de operadores
    print("\n2. SOBRECARGA DE OPERADORES:")
    print("-" * 40)
    
    class NumeroPersonalizado:
        def __init__(self, valor):
            self.valor = valor
            
        def __add__(self, outro):
            return NumeroPersonalizado(self.valor + outro.valor)
        
        def __sub__(self, outro):
            return NumeroPersonalizado(self.valor - outro.valor)
        
        def __str__(self):
            return str(self.valor)
    
    a = NumeroPersonalizado(5)
    b = NumeroPersonalizado(3)
    c = a + b  # Chama o método __add__
    d = a - b  # Chama o método __sub__
    
    print(f"Sobrecarga: {a} + {b} = {c}")
    print(f"Sobrecarga: {a} - {b} = {d}")

# =============================================================================
# ESTRUTURAS DE CONTROLE
# =============================================================================

def demonstrar_estruturas_controle():
    """Demonstra estruturas de controle condicionais e de repetição"""
    print("\n" + "=" * 60)
    print("ESTRUTURAS DE CONTROLE")
    print("=" * 60)
    
    # Comandos condicionais
    print("\n1. COMANDOS CONDICIONAIS:")
    print("-" * 40)
    
    idade = 18
    
    # if-elif-else
    if idade < 12:
        categoria = "Criança"
    elif idade < 18:
        categoria = "Adolescente"
    elif idade < 60:
        categoria = "Adulto"
    else:
        categoria = "Idoso"
    
    print(f"Idade {idade}: {categoria}")
    
    # Operador ternário
    status = "Maior de idade" if idade >= 18 else "Menor de idade"
    print(f"Status: {status}")
 
    # Comandos de repetição
    print("\n3. COMANDOS DE REPETIÇÃO:")
    print("-" * 40)
    
    # for loop
    print("For loop:")
    frutas = ["maçã", "banana", "laranja"]
    for fruta in frutas:
        print(f"  - {fruta}")
    
    # for com range
    print("\nFor com range:")
    for i in range(3):  # 0 a 2
        print(f"  Número: {i}")
    
    # for com enumerate
    print("\nFor com enumerate:")
    for indice, fruta in enumerate(frutas):
        print(f"  Índice {indice}: {fruta}")
    
    # while loop
    print("\nWhile loop:")
    contador = 3
    while contador > 0:
        print(f"  Contagem: {contador}")
        contador -= 1
    
    # break e continue
    print("\nUso de break e continue:")
    for numero in range(10):
        if numero == 2:
            continue  # Pula o número 2
        if numero == 7:
            break     # Para o loop no número 7
        print(f"  Número: {numero}")
    
    # else em loops
    print("\nElse em loops:")
    for numero in range(3):
        print(f"  Loop: {numero}")
    else:
        print("  Loop concluído sem interrupções")

# =============================================================================
# PALAVRAS RESERVADAS
# =============================================================================

def demonstrar_palavras_reservadas():
    """Demonstra o uso de palavras reservadas do Python"""
    print("\n" + "=" * 60)
    print("PALAVRAS RESERVADAS")
    print("=" * 60)
    
    # Lista de algumas palavras reservadas importantes
    palavras_reservadas = [
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
        'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
        'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
        'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
        'while', 'with', 'yield'
    ]
    
    print("Palavras reservadas do Python:")
    for i, palavra in enumerate(palavras_reservadas, 1):
        print(f"  {i:2d}. {palavra}")
    
    # Exemplo de uso de algumas palavras reservadas
    print("\nExemplos de uso:")
    
    # and, or, not
    resultado_logico = True and False or not True
    print(f"True and False or not True = {resultado_logico}")
    
    # if, elif, else
    valor = 10
    if valor > 5:
        print(f"{valor} é maior que 5")
    elif valor == 5:
        print(f"{valor} é igual a 5")
    else:
        print(f"{valor} é menor que 5")
    
    # for, in
    print("Loop for:")
    for i in range(3):
        print(f"  Iteração {i}")
    
    # while
    print("Loop while:")
    contador = 0
    while contador < 3:
        print(f"  Contador: {contador}")
        contador += 1
    
    # try, except, finally
    print("Tratamento de exceções:")
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        print("  Erro: Divisão por zero!")
    finally:
        print("  Bloco finally sempre executa")
    
    # return
    def exemplo_return():
        return "Valor retornado da função"
    
    print(f"Função com return: {exemplo_return()}")

# =============================================================================
# FUNÇÃO PRINCIPAL
# =============================================================================

def main():
    """Função principal que executa todas as demonstrações"""
    print("DEMONSTRAÇÃO DAS CARACTERÍSTICAS DO PYTHON")
    print("=" * 60)
    
    demonstrar_tipos_dados()
    demonstrar_referencias_variaveis()
    demonstrar_expressoes()
    demonstrar_estruturas_controle()
    demonstrar_palavras_reservadas()
    
    print("\n" + "=" * 60)
    print("FIM DA DEMONSTRAÇÃO")
    print("=" * 60)

# Executa a função principal se o arquivo for executado diretamente
if __name__ == "__main__":
    main()