import ply.lex as lex

# Lista de tokens da linguagem
tokens = (
    'QUANDO', 'BANDEIRA', 'CLICADA',
    'MOVA', 'PASSOS',
    'VIRE', 'DIREITA', 'ESQUERDA', 'GRAUS',
    'SE', 'ENTAO', 'FIM',
    'DIGA', 'STRING',
    'ESPERE', 'NUMERO', 'SEGUNDO',
    'REPITA', 'VEZES',
    'MUDE_COR_PARA',
    # Condições (sensores)
    'TOCANDO_BORDA', 'PRESSIONANDO_TECLA', 'TOCANDO_COR'
)

# Tokens fixos (palavras-chave)
t_QUANDO          = r'quando'
t_BANDEIRA        = r'bandeira'
t_CLICADA         = r'clicada'
t_MOVA            = r'mova'
t_PASSOS          = r'passos'
t_VIRE            = r'vire'
t_DIREITA         = r'direita'
t_ESQUERDA        = r'esquerda'
t_GRAUS           = r'graus'
t_SE              = r'se'
t_ENTAO           = r'entao'
t_FIM             = r'fim'
t_DIGA            = r'diga'
t_ESPERE          = r'espere'
t_SEGUNDO         = r'segundo'
t_REPITA          = r'repita'
t_VEZES           = r'vezes'
t_MUDE_COR_PARA   = r'mude_cor_para'
t_TOCANDO_BORDA   = r'tocando_borda'
t_PRESSIONANDO_TECLA = r'pressionando_tecla'
t_TOCANDO_COR     = r'tocando_cor'

# Regra para número (inteiro)
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regra para string entre aspas duplas (sem quebrar linha)
def t_STRING(t):
    r'\"([^"\n]*)\"'
    t.value = t.value[1:-1]  # Remove aspas
    return t

# Ignorar espaços, tabs e retorno de carro (Windows)
t_ignore = ' \t\r'

# Contar linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Erro de token
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()
