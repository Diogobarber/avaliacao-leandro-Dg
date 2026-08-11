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

# Empresta um livro

def emprestar_livro(livros):
    print("\n--- EMPRESTAR LIVRO ---")

    isbn = pedir_texto("ISBN do livro: ")

    livro = buscar_por_isbn(livros, isbn)

    if livro is None:
        print("Nenhum livro encontrado com esse ISBN.")
        return False

    if livro["status"].lower() == "emprestado":
        print("Este livro já está emprestado.")
        return False

    livro["status"] = "emprestado"

    salvar_livros(livros)

    print("Empréstimo registrado com sucesso.")

    return True    

# Devolve um livro

def devolver_livro(livros):
    print("\n--- DEVOLVER LIVRO ---")

    isbn = pedir_texto("ISBN do livro: ")

    livro = buscar_por_isbn(livros, isbn)

    if livro is None:
        print("Nenhum livro encontrado com esse ISBN.")
        return False

    if livro["status"].lower() == "disponivel":
        print("Este livro já está disponível.")
        return False

    livro["status"] = "disponivel"

    salvar_livros(livros)

    print("Devolução registrada com sucesso.")

    return True

# Lista todos os livros

def listar_livros(livros):
    print("\n--- LISTA DE LIVROS ---")

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    for livro in livros:
        print("------------------------------")
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])
        print("ISBN:", livro["isbn"])
        print("Status:", livro["status"])

    print("------------------------------")

# Busca um livro

def buscar_livro(livros):
    print("\n--- BUSCAR LIVRO ---")

    termo = pedir_texto(
        "Digite o título, autor ou ISBN: "
    ).lower()

    encontrados = []

    for livro in livros:
        if (
            termo in livro["titulo"].lower()
            or termo in livro["autor"].lower()
            or termo in livro["isbn"].lower()
        ):
            encontrados.append(livro)

    if len(encontrados) == 0:
        print("Nenhum livro encontrado.")
        return

    print("\nLivros encontrados:")

    for livro in encontrados:
        print("------------------------------")
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])
        print("ISBN:", livro["isbn"])
        print("Status:", livro["status"])

    print("------------------------------")

# Exibe o menu principal

def exibir_menu():
    print("\n========== BIBLIOTECA ==========")
    print("1 - Cadastrar livro")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Listar livros")
    print("5 - Buscar livro")
    print("0 - Sair")
    print("================================")


# Programa principal

livros = carregar_livros()

while True:
    exibir_menu()

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_livro(livros)

    elif opcao == "2":
        emprestar_livro(livros)

    elif opcao == "3":
        devolver_livro(livros)

    elif opcao == "4":
        listar_livros(livros)

    elif opcao == "5":
        buscar_livro(livros)

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Escolha uma opção do menu.")