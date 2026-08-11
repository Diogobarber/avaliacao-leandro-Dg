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