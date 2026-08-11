# Sistema de Gerenciamento de Biblioteca

## Sobre o código

O Sistema de Gerenciamento de Biblioteca é um programa desenvolvido em Python para auxiliar no controle de livros de uma biblioteca.

O sistema permite cadastrar novos livros e manter organizadas informações como título, autor, ano de publicação, ISBN e situação do livro. Também é possível consultar os livros cadastrados, realizar empréstimos e registrar devoluções.

Uma das preocupações do projeto foi fazer com que os dados não fossem perdidos quando o programa fosse encerrado. Para isso, os livros são armazenados no arquivo `biblioteca.csv`, que é utilizado pelo programa para carregar as informações quando ele é iniciado e para atualizar os dados sempre que alguma alteração é realizada.

O projeto foi desenvolvido utilizando conceitos trabalhados na disciplina de Lógica de Programação, principalmente funções, listas, dicionários, estruturas de repetição, estruturas condicionais, entrada e saída de dados e manipulação de arquivos.

---

## Objetivo

O objetivo do projeto é criar uma aplicação simples, funcional e organizada para controlar os livros de uma biblioteca através do terminal.

Através do menu principal, o usuário pode escolher a operação que deseja realizar sem precisar alterar o código do programa.

O sistema também possui algumas validações para evitar problemas durante o cadastro e durante as operações com os livros. Por exemplo, não é permitido cadastrar um livro sem preencher os campos necessários ou utilizar um ISBN que já esteja cadastrado.

---

## Como executar

Para utilizar o programa, é necessário ter o **Python** instalado no computador.

### 1. Baixar o projeto

Faça o download ou clone este repositório para o computador.

### 2. Abrir a pasta do projeto

Abra o terminal dentro da pasta onde estão os arquivos `main.py` e `biblioteca.csv`.

### 3. Executar o programa

No terminal, utilize:

```text
python main.py ou clique na setinha acima
