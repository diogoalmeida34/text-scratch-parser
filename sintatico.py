import ply.yacc as yacc
from lexer import tokens

# Classe para representar comandos
class Comando:
    def __init__(self, tipo, valor=None):
        self.tipo = tipo
        self.valor = valor

    def __repr__(self):
        return f"Comando({self.tipo}, {self.valor})"

# Lista global de comandos parseados
comandos = []

def p_programa(p):
    'programa : QUANDO evento comandos FIM'
    p[0] = ('programa', p[3])
    global comandos
    comandos = p[3]

def p_evento(p):
    '''evento : BANDEIRA CLICADA
              | BANDEIRA'''
    p[0] = 'bandeira clicada'

def p_comandos_lista(p):
    '''comandos : comandos comando'''
    p[0] = p[1] + [p[2]]

def p_comandos_unitario(p):
    '''comandos : comando'''
    p[0] = [p[1]]

# Comandos Movimento
def p_comando_mova(p):
    'comando : MOVA NUMERO PASSOS'
    p[0] = Comando('mova', p[2])

def p_comando_vire_direita(p):
    'comando : VIRE DIREITA NUMERO GRAUS'
    p[0] = Comando('vire_direita', p[3])

def p_comando_vire_esquerda(p):
    'comando : VIRE ESQUERDA NUMERO GRAUS'
    p[0] = Comando('vire_esquerda', p[3])

def p_comando_mude_cor(p):
    'comando : MUDE_COR_PARA STRING'
    p[0] = Comando('mude_cor', p[2])

# Comandos auxiliares
def p_comando_diga(p):
    'comando : DIGA STRING'
    p[0] = Comando('diga', p[2])

def p_comando_espere(p):
    'comando : ESPERE NUMERO SEGUNDO'
    p[0] = Comando('espere', p[2])

# Controle
def p_comando_se(p):
    'comando : SE condicao ENTAO comandos FIM'
    p[0] = Comando('se', (p[2], p[4]))

def p_comando_repita(p):
    'comando : REPITA NUMERO VEZES comandos FIM'
    p[0] = Comando('repita', (p[2], p[4]))

# Condições (sensores)
def p_condicao_tocando_borda(p):
    'condicao : TOCANDO_BORDA'
    p[0] = ('tocando_borda',)

def p_condicao_pressionando_tecla(p):
    'condicao : PRESSIONANDO_TECLA STRING'
    p[0] = ('pressionando_tecla', p[2])

def p_condicao_tocando_cor(p):
    'condicao : TOCANDO_COR STRING'
    p[0] = ('tocando_cor', p[2])

def p_error(p):
    if p:
        print(f"Erro sintático na linha {p.lineno}: token inesperado '{p.value}'")
    else:
        print("Erro sintático: fim inesperado do arquivo")
    # Retorna None para indicar erro
    raise SyntaxError("Erro sintático detectado")

parser = yacc.yacc()
