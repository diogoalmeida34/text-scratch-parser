import json
import os
from datetime import datetime

os.makedirs("testes-logs", exist_ok=True)
os.makedirs("testes-json", exist_ok=True)

class EstadoAtor:
    def __init__(self):
        self.posicao = 0
        self.direcao = 0
        self.cor = "preto"
        self.log = []

    def registrar(self, mensagem, tipo="info", nivel_indent=0):
        # Remove indentação interna na mensagem (espaços à esquerda)
        mensagem_sem_indent = mensagem.lstrip()
        registro = {
            "timestamp": datetime.now().isoformat(),
            "tipo": tipo,
            "mensagem": mensagem_sem_indent,
            "nivel_indent": nivel_indent
        }
        self.log.append(registro)

    def __repr__(self):
        return f"EstadoAtor(posicao={self.posicao}, direcao={self.direcao}, cor={self.cor})"


def interpretar_condicao(condicao, estado):
    if not isinstance(condicao, (tuple, list)) or len(condicao) == 0:
        estado.registrar(f"Condição inválida: {condicao}", tipo="erro")
        return False

    tipo = condicao[0]
    if tipo == 'tocando_borda':
        cond = estado.posicao >= 100
        estado.registrar(f"Condição tocando_borda → {cond}", tipo="condicao")
        return cond
    elif tipo == 'pressionando_tecla':
        if len(condicao) < 2:
            estado.registrar("Condição pressionando_tecla inválida (falta tecla)", tipo="erro")
            return False
        tecla = condicao[1]
        estado.registrar(f"Condição pressionando_tecla '{tecla}' → False (simulado)", tipo="condicao")
        return False
    elif tipo == 'tocando_cor':
        if len(condicao) < 2:
            estado.registrar("Condição tocando_cor inválida (falta cor)", tipo="erro")
            return False
        cor = condicao[1]
        cond = estado.cor == cor
        estado.registrar(f"Condição tocando_cor '{cor}' → {cond}", tipo="condicao")
        return cond
    else:
        estado.registrar(f"Condição desconhecida '{tipo}'", tipo="erro")
        return False


def interpretar_comandos(lista, estado, nivel=0):
    for comando in lista:
        estado.registrar(f"Executando comando '{getattr(comando, 'tipo', str(comando))}'", tipo="execucao", nivel_indent=nivel)
        try:
            if not hasattr(comando, 'tipo'):
                estado.registrar(f"Comando inválido ignorado: {comando}", tipo="erro", nivel_indent=nivel)
                continue

            if comando.tipo == 'mova':
                estado.posicao += comando.valor
                estado.registrar(f"Movendo {comando.valor} passos → posição agora: {estado.posicao}", tipo="movimento", nivel_indent=nivel)

            elif comando.tipo == 'vire_direita':
                estado.direcao = (estado.direcao + comando.valor) % 360
                estado.registrar(f"Virando à direita {comando.valor} graus → direção agora: {estado.direcao}", tipo="movimento", nivel_indent=nivel)

            elif comando.tipo == 'vire_esquerda':
                estado.direcao = (estado.direcao - comando.valor) % 360
                estado.registrar(f"Virando à esquerda {comando.valor} graus → direção agora: {estado.direcao}", tipo="movimento", nivel_indent=nivel)

            elif comando.tipo == 'mude_cor':
                estado.cor = comando.valor
                estado.registrar(f"Mudando cor para {comando.valor}", tipo="movimento", nivel_indent=nivel)

            elif comando.tipo == 'diga':
                estado.registrar(f'Diz: "{comando.valor}"', tipo="saida", nivel_indent=nivel)

            elif comando.tipo == 'espere':
                estado.registrar(f"Esperando {comando.valor} segundo(s)", tipo="tempo", nivel_indent=nivel)

            elif comando.tipo == 'se':
                if not isinstance(comando.valor, (tuple, list)) or len(comando.valor) != 2:
                    estado.registrar(f"Comando 'se' mal formado: {comando.valor}", tipo="erro", nivel_indent=nivel)
                    continue
                cond, blocos = comando.valor
                estado.registrar(f"Avaliando condição 'se'", tipo="controle", nivel_indent=nivel)
                if interpretar_condicao(cond, estado):
                    interpretar_comandos(blocos, estado, nivel + 1)
                else:
                    estado.registrar(f"Condição falsa — bloco 'se' ignorado", tipo="controle", nivel_indent=nivel)

            elif comando.tipo == 'repita':
                if not isinstance(comando.valor, (tuple, list)) or len(comando.valor) != 2:
                    estado.registrar(f"Comando 'repita' mal formado: {comando.valor}", tipo="erro", nivel_indent=nivel)
                    continue
                vezes, blocos = comando.valor
                estado.registrar(f"Iniciando repetição {vezes} vezes", tipo="controle", nivel_indent=nivel)
                for i in range(vezes):
                    estado.registrar(f"Repetição {i+1} de {vezes}", tipo="controle", nivel_indent=nivel)
                    interpretar_comandos(blocos, estado, nivel + 1)

            else:
                estado.registrar(f"Comando desconhecido '{comando.tipo}' ignorado", tipo="erro", nivel_indent=nivel)

        except Exception as e:
            estado.registrar(f"Erro ao executar comando '{getattr(comando, 'tipo', 'desconhecido')}': {e}", tipo="erro", nivel_indent=nivel)

def salvar_log_e_json(estado):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    logfile = f"testes-logs/exec_log_{timestamp}.log"
    jsonfile = f"testes-json/exec_result_{timestamp}.json"

    with open(logfile, 'w', encoding='utf-8') as f:
        for registro in estado.log:
            tipo_formatado = f"[{registro['tipo']}]".ljust(12)
            indent = "  " * registro.get("nivel_indent", 0)
            linha = f"[{registro['timestamp']}] {tipo_formatado} {indent}{registro['mensagem']}\n"
            f.write(linha)

    with open(jsonfile, 'w', encoding='utf-8') as f:
        json.dump({
            "estado_final": {
                "posicao": estado.posicao,
                "direcao": estado.direcao,
                "cor": estado.cor
            },
            "log": estado.log
        }, f, indent=4, ensure_ascii=False)

    print(f"\n Log salvo em {logfile}")
    print(f" Resultado JSON salvo em {jsonfile}")

    return logfile, jsonfile


def imprimir_log(log):
    for registro in log:
        tipo_formatado = f"[{registro['tipo']}]".ljust(12)
        indent = "  " * registro.get("nivel_indent", 0)
        print(f"[{registro['timestamp']}] {tipo_formatado} {indent}{registro['mensagem']}")


def interpretar(comandos):
    estado = EstadoAtor()
    estado.registrar("Iniciando interpretação...", tipo="info", nivel_indent=0)
    interpretar_comandos(comandos, estado)
    estado.registrar("\nEstado final do ator:", tipo="info", nivel_indent=0)
    estado.registrar(repr(estado), tipo="info", nivel_indent=0)
    salvar_log_e_json(estado)

    imprimir_log(estado.log)

    return estado
