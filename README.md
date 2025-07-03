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
project2-GRULFAT/
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
├── interprete.py               # Interpretador que executa comandos da AST
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

- **Logs**: Arquivos gerados na pasta `testes-logs/` detalham cada comando executado, incluindo o estado do ator (posição, direção, etc.) em cada passo.
- **JSON**: Arquivos na pasta `testes-json/` contêm o estado final do ator (posição, cor, direção) e o log completo da execução, permitindo integração com outras ferramentas ou análises posteriores.

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

## Referências

- Scratch: https://scratch.mit.edu  
- PLY (Python Lex-Yacc): https://www.dabeaz.com/ply/  
- Documentação Python: https://docs.python.org/3/  
