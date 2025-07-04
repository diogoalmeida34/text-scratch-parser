import sys
import time
from sintatico import parser
from interprete import interpretar_comandos, EstadoAtor
import json
import os
from datetime import datetime

def executar_codigo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        codigo = f.read()

    print(f"Código lido:\n{codigo}")
    print("\nIniciando parser...")

    try:
        resultado = parser.parse(codigo)
    except SyntaxError as e:
        print(f"Erro sintático detectado: {e}")
        return None, EstadoAtor(), ["Erro sintático detectado"]

    if not resultado or len(resultado) < 2:
        print("Nenhum comando reconhecido.\n")
        return None, EstadoAtor(), ["Nenhum comando reconhecido."]

    comandos = resultado[1]

    print("Comandos interpretados:")
    estado = EstadoAtor()
    print("Iniciando interpretação...")
    interpretar_comandos(comandos, estado)

    print("\nEstado final do ator:")
    print(repr(estado))

    os.makedirs("testes-logs", exist_ok=True)
    os.makedirs("testes-json", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    logfile = f"testes-logs/exec_log_{timestamp}.log"
    jsonfile = f"testes-json/exec_result_{timestamp}.json"

    with open(logfile, 'w', encoding='utf-8') as f:
        for registro in estado.log:
            linha = f"[{registro['timestamp']}] [{registro['tipo']}] {registro['mensagem']}"
            f.write(linha + "\n")

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
    print(f"Resultado JSON salvo em {jsonfile}")

    return comandos, estado, estado.log

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python main.py arquivo.scratch")
        sys.exit(1)

    arquivo = sys.argv[1]

    total_testes = 1
    sucesso = 0
    falhas = 0

    start_time = time.time()

    try:
        comandos_parseados, estado_final, log = executar_codigo(arquivo)

        if comandos_parseados is None:
            # Parser falhou, já avisamos no executar_codigo
            falhas = 1
        else:
            for registro in log:
                print(f"[{registro['timestamp']}] [{registro['tipo']}] {registro['mensagem']}")
            sucesso = 1
    except FileNotFoundError:
        print(f"Arquivo '{arquivo}' não encontrado.")
        falhas = 1
    except Exception as e:
        print(f"Erro inesperado: {e}")
        falhas = 1

    tempo_total = time.time() - start_time

    print("\n==============================")
    print("TESTES CONCLUÍDOS")
    print(f"Total de testes: {total_testes}")
    print(f"Sucesso: {sucesso}")
    print(f"Falhas: {falhas}")
    print(f"Tempo total: {tempo_total:.2f}s")
    print("==============================")
