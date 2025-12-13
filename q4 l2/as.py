import re

class Parser:
    def __init__(self, input_str):
        self.tokens = self.tokenize(input_str)
        self.pos = 0
    
    def tokenize(self, s):
        token_spec = [
            ('ID', r'[a-zA-Z][a-zA-Z0-9_]*'),
            ('NUM', r'\d+'),
            ('STRING', r'\'[^\']*\'|\"[^\"]*\"'),
            ('COMP_OP', r'==|!=|>|<|>=|<='),
            ('COLON', r':'),
            ('LBRACKET', r'\['),
            ('RBRACKET', r'\]'),
            ('WHITESPACE', r'\s+'),
        ]
        token_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_spec)
        tokens = []
        for mo in re.finditer(token_regex, s):
            kind = mo.lastgroup
            value = mo.group()
            if kind != 'WHITESPACE':
                tokens.append((kind, value))
        return tokens
    
    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ('EOF', '')
    
    def match(self, expected_kind, expected_value=None):
        kind, value = self.current_token()
        if kind == expected_kind and (expected_value is None or value == expected_value):
            self.pos += 1
            return value
        else:
            raise SyntaxError(f'Esperado {expected_kind}, encontrado {kind} ({value})')
    
    
    def parse(self):
        self.S()
        if self.pos != len(self.tokens):
            raise SyntaxError('Tokens extras após análise completa')
        print("Cadeia aceita com sucesso.")
    
    def S(self):
        self.ID()
        self.match('LBRACKET')
        self.INDEX()
        self.match('RBRACKET')
    
    def ID(self):
        self.match('ID')
    
    def INDEX(self):
        kind, value = self.current_token()
        if kind == 'NUM':
            if self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1][0] == 'COLON':
                self.NUM_SLICE()
            else:
                self.I()
        elif kind in ('STRING',):
            if self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1][0] == 'COLON':
                self.NAME_SLICE()
            else:
                self.ST()
        elif kind == 'ID':
            if self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1][0] == 'LBRACKET':
                self.ACCESS()
                kind2, _ = self.current_token()
                if kind2 == 'COMP_OP':
                    self.COMPARE_continuation()
            else:
                self.ID()
        elif kind == 'COLON':
            self.NAME_SLICE()
        else:
            raise SyntaxError(f'INDEX inesperado: {kind}')
    
    def I(self):
        self.match('NUM')
    
    def ST(self):
        self.match('STRING')
    
    def NUM_SLICE(self):
        self.NUM_OPT()
        self.match('COLON')
        self.NUM_OPT()
    
    def NUM_OPT(self):
        kind, _ = self.current_token()
        if kind == 'NUM':
            self.I()
    
    def NAME_SLICE(self):
        self.NAME_OPT()
        self.match('COLON')
        self.NAME_OPT()
    
    def NAME_OPT(self):
        kind, _ = self.current_token()
        if kind == 'ID':
            self.ID()
        elif kind == 'STRING':
            self.ST()
    
    def ACCESS(self):
        self.ID()
        self.match('LBRACKET')
        self.INDEX()
        self.match('RBRACKET')
    
    def COMPARE_continuation(self):
        self.match('COMP_OP')
        self.RHS()
    
    def RHS(self):
        kind, _ = self.current_token()
        if kind == 'NUM':
            self.I()
        elif kind == 'STRING':
            self.ST()
        elif kind == 'ID':
            if self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1][0] == 'LBRACKET':
                self.ACCESS()
            else:
                self.ID()
        else:
            raise SyntaxError(f'RHS inesperado: {kind}')

# testando

exemplos = [
    "X[123456]",
    "X['CPF']",
    "X[0:10]",
    "X[:'DATA']",
    "X[Y[2:3]]",
    "X[Y['MES'] <= 4]"
]

for i, ex in enumerate(exemplos, 1):
    print(f"\n--- Exemplo {i}: {ex} ---")
    try:
        parser = Parser(ex)
        parser.parse()
    except SyntaxError as e:
        print(f"Erro de sintaxe: {e}")