# Projeto 2 – Linguagem Textual Inspirada no Scratch (GRULFAT)

## Equipe
**Disciplina:** GRULFAT – Linguagens Formais e Autômatos\
**Curso:** Bacharelado em Engenharia de Computação

**Desenvolvedores**: \
• Carolina Yumi Siroma -  GU3042049\
• Celine Galdino Da Silva - GU3046354\
• Diogo Da Silva Almeida - GU3059995

**Professores Orientadores:** \
• Doutor Thiago Schumacher Barcelos \
• Doutora Alexandra Aparecida de Souza

---

## Objetivo

Este projeto implementa um lexer, parser e interpretador para uma linguagem textual inspirada no Scratch, voltada para iniciantes e aprendizado de programação. A linguagem permite programar comandos de movimento, controle e sensores, simulando um ator que pode se mover, virar, falar, esperar e reagir a condições.

O projeto foi desenvolvido para a disciplina GRULFAT, atendendo aos critérios de avaliação de sintaxe, execução, criatividade e usabilidade.

---

## Estrutura do Projeto

```
text-scratch-parser/
│
├── exemplos_scratch/           # Arquivos de código-fonte em linguagem textual (.scratch)
│   ├── exemplo1.scratch
│   ├── exemplo2.scratch
│   ├── exemplo3.scratch
│   ├── exemplo4.scratch
│   └── exemplo5.scratch
│
├── testes-logs/                # Logs gerados após execução dos programas
│
├── testes-json/                # Resultados em JSON gerados após execução
│
├── lexer.py                    # Analisador léxico (tokenizador)
├── sintatico.py                # Analisador sintático (parser) com gramática
├── interprete.py               # Interpretador que executa comandos da AST e gera logs detalhados com indentação hierárquica para estruturas de controle (condicionais e repetições)
├── main.py                     # Script principal para executar um programa .scratch
├── rodar_testes.py             # Script para executar automaticamente todos os exemplos
└── README.md                   # Documentação do projeto (este arquivo)
```

---

## Requisitos

- **Python** 3.8 ou superior
- **Biblioteca PLY** para análise léxica e sintática

### Instalação
Instale as dependências necessárias:

```bash
pip install ply
```

---

## Como Executar um Programa .scratch

Para executar um programa textual individual:

```bash
python main.py exemplos_scratch/exemplo1.scratch
```

### Etapas realizadas:
1. Lê o código-fonte do arquivo .scratch
2. Realiza análise léxica e sintática
3. Interpreta os comandos a partir da AST (Abstract Syntax Tree)
4. Exibe a execução passo a passo no console
5. Salva logs detalhados na pasta `testes-logs/`
6. Exporta o estado final e log em formato JSON na pasta `testes-json/`

---

## Como Executar Todos os Testes Automatizados

Para rodar todos os arquivos .scratch na pasta `exemplos_scratch` e gerar logs e JSONs:

```bash
python rodar_testes.py
```

---

## Descrição da Linguagem Textual Inspirada no Scratch

### Estrutura Básica
- **Evento inicializador**: `quando bandeira clicada` inicia a execução do programa.

### Comandos de Movimento
- `mova <n> passos`: Move o ator n passos na direção atual.
- `vire direita <n> graus`: Gira o ator n graus à direita.
- `vire esquerda <n> graus`: Gira o ator n graus à esquerda.
- `mude_cor_para "<cor>"`: Altera a cor do ator para a especificada.

### Comandos Auxiliares
- `diga "<texto>"`: Exibe uma mensagem no console.
- `espere <n> segundo(s)`: Pausa a execução por n segundos.

### Comandos de Controle
- **Condicional**:
  ```plaintext
  se <condicao> entao
      <comandos>
  fim
  ```
- **Repetição**:
  ```plaintext
  repita <n> vezes
      <comandos>
  fim
  ```

### Condições (Sensores)
- `tocando_borda`: Verifica se o ator está na borda da área de execução.
- `pressionando_tecla "<tecla>"`: Verifica se uma tecla específica está pressionada.
- `tocando_cor "<cor>"`: Verifica se o ator está em contato com uma cor específica.

### Exemplo de Programa
```plaintext
quando bandeira clicada
    mova 10 passos
    vire direita 15 graus
    se tocando_borda entao
        diga "Estou na borda"
    fim
    repita 3 vezes
        diga "Oi!"
        espere 1 segundo
    fim
    mude_cor_para "vermelho"
fim
```

---

## Logs e Exportação JSON

### Logs
Os arquivos de log são gerados na pasta `testes-logs/` e detalham cada comando executado durante a interpretação de um programa. A indentação reflete a hierarquia dos blocos de controle, como `se` e `repita`, facilitando a leitura e a depuração. Cada entrada no log inclui:

- O timestamp da execução.
- O tipo de ação (execucao, saida, controle, condicao, movimento, tempo, etc.).
- A mensagem descrevendo o comando ou ação realizada.
- O nível de indentação para refletir a hierarquia.

### Exemplo de Log com Indentação
```
[2025-07-03T00:08:14.372400] [execucao]   Executando comando 'diga'
[2025-07-03T00:08:14.372400] [saida]      Diz: "Vamos testar condições..."
[2025-07-03T00:08:14.372400] [execucao]   Executando comando 'se'
[2025-07-03T00:08:14.372400] [controle]   Avaliando condição 'se'
[2025-07-03T00:08:14.372400] [condicao]   Condição pressionando_tecla 'seta_cima' → False (simulado)
[2025-07-03T00:08:14.372400] [controle]   Condição falsa — bloco 'se' ignorado
[2025-07-03T00:08:14.372400] [execucao]   Executando comando 'se'
[2025-07-03T00:08:14.372400] [controle]   Avaliando condição 'se'
[2025-07-03T00:08:14.372400] [condicao]   Condição tocando_cor 'preto' → True
[2025-07-03T00:08:14.372400] [execucao]     Executando comando 'diga'
[2025-07-03T00:08:14.372400] [saida]        Diz: "Estou na cor preta!"
[2025-07-03T00:08:14.372400] [execucao]   Executando comando 'mude_cor'
[2025-07-03T00:08:14.372400] [movimento]  Mudando cor para rosa
[2025-07-03T00:08:14.372400] [execucao]   Executando comando 'vire_esquerda'
[2025-07-03T00:08:14.372400] [movimento]  Virando à esquerda 45 graus → direção agora: 315
[2025-07-03T00:08:14.372400] [execucao]   Executando comando 'espere'
[2025-07-03T00:08:14.372400] [tempo]      Esperando 1 segundo(s)
[2025-07-03T00:08:14.372400] [execucao]   Executando comando 'diga'
[2025-07-03T00:08:14.372400] [saida]      Diz: "Pronto!"
```

---

### JSON
Os arquivos JSON são gerados na pasta `testes-json/` e contêm duas seções principais:
- **estado_final**: O estado final do ator após a execução do programa, incluindo posição, cor e direção.
- **log**: O log completo da execução, detalhando cada comando ou ação executada, com timestamp, tipo, mensagem e nível de indentação.

### Exemplo de Estrutura JSON
```json
{
    "estado_final": {
        "posicao": 0,
        "direcao": 315,
        "cor": "rosa"
    },
    "log": [
        {
            "timestamp": "2025-07-03T00:08:14.372400",
            "tipo": "execucao",
            "mensagem": "Executando comando 'diga'",
            "nivel_indent": 0
        },
        {
            "timestamp": "2025-07-03T00:08:14.372400",
            "tipo": "saida",
            "mensagem": "Diz: \"Vamos testar condições...\"",
            "nivel_indent": 0
        },
        {
            "timestamp": "2025-07-03T00:08:14.372400",
            "tipo": "execucao",
            "mensagem": "Executando comando 'se'",
            "nivel_indent": 0
        },
        {
            "timestamp": "2025-07-03T00:08:14.372400",
            "tipo": "controle",
            "mensagem": "Avaliando condição 'se'",
            "nivel_indent": 0
        },
        {
            "timestamp": "2025-07-03T00:08:14.372400",
            "tipo": "condicao",
            "mensagem": "Condição pressionando_tecla 'seta_cima' → False (simulado)",
            "nivel_indent": 0
        },
        {
            "timestamp": "2025-07-03T00:08:14.372400",
            "tipo": "controle",
            "mensagem": "Condição falsa — bloco 'se' ignorado",
            "nivel_indent": 0
        },
        {
            "timestamp": "2025-07-03T00:08:14.372400",
            "tipo": "execucao",
            "mensagem": "Executando comando 'se'",
            "nivel_indent": 0
        },
        {
            "timestamp": "2025-07-03T00:08:14.372400",
            "tipo": "controle",
            "mensagem": "Avaliando condição 'se'",
            "nivel_indent": 0
        },
        {
            "timestamp": "2025-07-03T00:08:14.372400",
            "tipo": "condicao",
            "mensagem": "Condição tocando_cor 'preto' → True",
            "nivel_indent": 0
        },
        {
            "timestamp": "2025-07-03T00:08:14.372400",
            "tipo": "execucao",
            "mensagem": "Executando comando 'diga'",
            "nivel_indent": 1
        },
        {
            "timestamp": "2025-07-03T00:08:14.372400",
            "tipo": "saida",
            "mensagem": "Diz: \"Estou na cor preta!\"",
            "nivel_indent": 1
        },
        {
            "timestamp": "2025-07-03T00:08:14.372400",
            "tipo": "execucao",
            "mensagem": "Executando comando 'mude_cor'",
            "nivel_indent": 0
        },
        {
            "timestamp": "2025-07-03T00:08:14.372400",
            "tipo": "movimento",
            "mensagem": "Mudando cor para rosa",
            "nivel_indent": 0
        },
        {
            "timestamp": "2025-07-03T00:08:14.372400",
            "tipo": "execucao",
            "mensagem": "Executando comando 'vire_esquerda'",
            "nivel_indent": 0
        },
        {
            "timestamp": "2025-07-03T00:08:14.372400",
            "tipo": "movimento",
            "mensagem": "Virando à esquerda 45 graus → direção agora: 315",
            "nivel_indent": 0
        },
        {
            "timestamp": "2025-07-03T00:08:14.372400",
            "tipo": "execucao",
            "mensagem": "Executando comando 'espere'",
            "nivel_indent": 0
        },
        {
            "timestamp": "2025-07-03T00:08:14.372400",
            "tipo": "tempo",
            "mensagem": "Esperando 1 segundo(s)",
            "nivel_indent": 0
        },
        {
            "timestamp": "2025-07-03T00:08:14.372400",
            "tipo": "execucao",
            "mensagem": "Executando comando 'diga'",
            "nivel_indent": 0
        },
        {
            "timestamp": "2025-07-03T00:08:14.372400",
            "tipo": "saida",
            "mensagem": "Diz: \"Pronto!\"",
            "nivel_indent": 0
        }
    ]
}
```

---

## Possíveis Extensões Futuras

- **Novos comandos**: Incluir movimentos diagonais, reprodução de sons ou animações.
- **Variáveis**: Suportar variáveis e expressões aritméticas para maior flexibilidade.
- **Controle avançado**: Adicionar condições com `senão` e operadores lógicos (e, ou, não).
- **Interface gráfica**: Criar uma visualização interativa para simular a execução do ator.
- **Exportação para Scratch**: Gerar código compatível com o Scratch visual a partir do texto.

---

## Visão Geral do Funcionamento

O sistema processa o código `.scratch` em etapas:

1. **Análise Léxica:** identifica os tokens (palavras-chave, números, strings).  
2. **Análise Sintática:** verifica a conformidade com a gramática definida, construindo uma Árvore Sintática Abstrata (AST).  
3. **Interpretação:** executa os comandos na AST, simulando o ator com estado interno (posição, direção, cor).  
4. **Logs e Exportação:** registra detalhadamente a execução em arquivos de log e JSON para análise posterior.

---

## Critérios de Avaliação Atendidos

- **Sintaxe Completa:** gramática abrangente cobrindo eventos, movimento, controle e sensores.  
- **Execução Correta:** interpretador executa comandos e condições conforme especificado.  
- **Documentação e Organização:** código comentado, estrutura clara e documentação detalhada.  
- **Automação:** script para executar todos os exemplos com geração de logs e JSON.  
- **Criatividade:** extensão da linguagem com novos comandos e condições, além da exportação estruturada.

---

## Como Clonar e Rodar o Projeto Localmente

```bash
git clone https://github.com/diogoalmeida34/text-scratch-parser.git

cd <nome-repositorio>

#Python 3.8 ou superior já instalado
python --version

# Instale as dependências necessárias:
pip install ply

# Este comando executa um único programa .scratch
python main.py exemplos_scratch/exemplo1.scratch

#OU

# Este comando executa automaticamente todos os arquivos .scratch encontrados na pasta exemplos_scratch/
python rodar_testes.py
```
---

## Referências

- Scratch: https://scratch.mit.edu  
- PLY (Python Lex-Yacc): https://www.dabeaz.com/ply/  
- Documentação Python: https://docs.python.org/3/
