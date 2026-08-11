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