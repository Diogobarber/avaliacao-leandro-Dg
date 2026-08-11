import csv

ARQUIVO = "biblioteca.csv"


# Carrega os livros salvos no arquivo CSV.

def carregar_livros():
    livros = []

    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                livros.append(linha)

    except FileNotFoundError:
        pass

    return livros

# Salva os livros no arquivo CSV

def salvar_livros(livros):
    campos = ["titulo", "autor", "ano", "isbn", "status"]
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(livros)

# Procura um livro pelo ISBN

def buscar_por_isbn(livros, isbn):
    for livro in livros:
        if livro["isbn"].lower() == isbn.lower():
            return livro

    return None

# Pede um texto e impede que o campo fique vazio

def pedir_texto(mensagem):
    while True:
        texto = input(mensagem).strip()

        if texto != "":
            return texto

        print("Este campo não pode ficar vazio.")

# Pede um ano válido

def pedir_ano():
    while True:
        ano_digitado = input("Ano: ").strip()

        if ano_digitado.isdigit():
            return ano_digitado

        print("Ano inválido. Digite apenas números.")

# Cadastra um livro novo

def cadastrar_livro(livros):
    print("\n--- CADASTRAR LIVRO ---")

    titulo = pedir_texto("Título: ")
    autor = pedir_texto("Autor: ")
    ano = pedir_ano()
    isbn = pedir_texto("ISBN: ")

    if buscar_por_isbn(livros, isbn) is not None:
        print("Este ISBN já está cadastrado.")
        return False

    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": isbn,
        "status": "disponivel"
    }

    livros.append(livro)
    salvar_livros(livros)

    print("Livro cadastrado com sucesso.")

    return True    