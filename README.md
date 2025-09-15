
# 💰 Gerenciador de Contas Mensais

Este é um programa simples em Python para gerenciar contas mensais, permitindo cadastrar, listar, excluir e exportar os dados para um arquivo Excel.

Ele organiza as contas por mês e permite registrar contas parceladas automaticamente nos meses seguintes.

## 🚀 Funcionalidades

- Adicionar conta

 - Registrar uma conta em um determinado mês.

- Caso seja parcelada, o sistema divide o valor pelas parcelas e adiciona automaticamente nos meses seguintes.

- Listar contas

- Exibir todas as contas registradas em um mês específico.

- Mostrar o total do mês.

- Deletar conta

- Remover uma conta de um mês selecionado pelo nome.

- Gerar Excel

- Exporta as contas mensais para um arquivo chamado contas_mensais.xlsx usando o Pandas.

- Sair

- Encerra o programa.


## 📋 Estrutura do Programa

O sistema utiliza uma lista de dicionários representando os meses do ano:

``` bash 
meses = [
    {"nome": "Janeiro", "contas": []},
    {"nome": "Fevereiro", "contas": []},
    {"nome": "Março", "contas": []},
    ...
    {"nome": "Dezembro", "contas": []},
]
````

Cada conta adicionada é armazenada assim:

```
{"nome": "Conta de Luz", "valor": 120.50}

```

## 🖥️ Menu Principal

```
--------------------------------------------------------
Menu:
1. Adicionar conta
2. Listar contas
3. Deletar conta
4. Sair
5. Gerar excel
--------------------------------------------------------

```

## 📦 Dependências

O projeto utiliza Python 3 e a biblioteca Pandas.

Instale as dependências com:

```
pip install pandas openpyxl

```
(O openpyxl é necessário para salvar em Excel).


## 📊 Saída em Excel

Ao escolher a opção 5, o programa gera um arquivo chamado:

```
contas_mensais.xlsx

```

Cada coluna representa um mês, e as linhas contêm os valores das contas registradas.

Exemplo:

Janeiro	Fevereiro	Março
120.50	200.00	150.00
80.00	100.00


## ▶️ Como Executar

Salve o código em um arquivo, por exemplo: gerenciador_contas.py

No terminal, execute:

```
python gerenciador_contas.py

```

Navegue pelo menu para gerenciar suas contas.

## 📌 Melhorias Futuras

Adicionar persistência dos dados em arquivo JSON ou banco de dados.

Criar relatórios automáticos de gastos mensais.

Implementar interface gráfica com Tkinter ou PyQt.

🔹 Projeto simples, mas útil para organização financeira pessoal.