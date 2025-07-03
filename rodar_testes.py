import os
import time
from datetime import datetime
from sintatico import parser
from interprete import EstadoAtor, interpretar_comandos, salvar_log_e_json

PASTA_EXEMPLOS = "exemplos_scratch"

def interpretar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        codigo = f.read()

    resultado = parser.parse(codigo)
    if not resultado or len(resultado) < 2:
        raise Exception("Nenhum comando reconhecido no arquivo.")

    comandos = resultado[1]

    estado = EstadoAtor()
    interpretar_comandos(comandos, estado)

    log_path, json_path = salvar_log_e_json(estado)
    return log_path, json_path

def main():
    print("Executando todos os testes em exemplos_scratch...\n")

    arquivos = sorted([
        f for f in os.listdir(PASTA_EXEMPLOS)
        if f.endswith(".scratch")
    ])

    total_testes = len(arquivos)
    testes_sucesso = 0
    testes_falha = 0

    tempo_inicio = time.time()

    for nome_arquivo in arquivos:
        caminho = os.path.join(PASTA_EXEMPLOS, nome_arquivo)
        print(f"Executando: {nome_arquivo}")

        try:
            log_path, json_path = interpretar_arquivo(caminho)

            print(f"\n Log salvo em {log_path}")
            print(f" Resultado JSON salvo em {json_path}")

            print("Teste concluído com sucesso.\n")
            testes_sucesso += 1

        except Exception as e:
            print(f"❌ Erro ao executar {nome_arquivo}: {e}")
            testes_falha += 1
            continue

    tempo_fim = time.time()
    duracao_total = tempo_fim - tempo_inicio

    print("\n" + "=" * 30)
    print("TESTES CONCLUÍDOS")
    print(f"Total de testes: {total_testes}")
    print(f"Sucesso: {testes_sucesso}")
    print(f"Falhas: {testes_falha}")
    print(f"Tempo total: {duracao_total:.2f}s")
    print("=" * 30)

if __name__ == "__main__":
    main()
