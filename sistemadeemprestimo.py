import csv

# Função para gravar os dados em um arquivo CSV
def grava_arquivo(type, dados):
    tipo = type.casefold()
    if tipo == "livro":
        arquivo = open("biblioteca.csv", "a")
        arquivo.write(f"{dados}" + "\n")
        arquivo.close()
        return
    elif tipo == "usuario":
        arquivo = open("usuarios.csv", "a")
        arquivo.write(f"{dados}" + "\n")
        arquivo.close()
        return
    elif tipo == "emprestimo":
        arquivo = open("emprestimos.csv", "a")
        arquivo.write(f"{dados}" + "\n")
        arquivo.close()
        return
    elif tipo == "categoria":
        arquivo = open("categorias.csv", "a")
        arquivo.write(f"{dados}" + "\n")
        arquivo.close()
        return
    elif tipo == "autor":
        arquivo = open("autor.csv", "a")
        arquivo.write(f"{dados}" + "\n")
        arquivo.close()
        return

# Função para verificar se um livro já está emprestado
def livro_emprestado(isbn):
    try:
        with open("emprestimos.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == isbn:
                    return True
        return False
    except FileNotFoundError:
        return False

# Função para associar um livro a um usuário com a data de empréstimo
def associar_livro_usuario(isbn, id_usuario, data_emprestimo):
    """Associa um livro a um usuário com a data de empréstimo."""
    if livro_emprestado(isbn):
        print(f"Erro: Livro {isbn} já emprestado.")
        return
    emprestimo = f"{isbn},{id_usuario},{data_emprestimo}"
    grava_arquivo("emprestimo", emprestimo)
    print(f"Livro {isbn} emprestado para o usuário {id_usuario} em {data_emprestimo}")

# Função para listar todos os empréstimos ativos
def listar_emprestimos_ativos():
    """Lista todos os empréstimos ativos."""
    try:
        with open("emprestimos.csv", "r") as file:
            reader = csv.reader(file)
            if not any(reader):
                print("Não há empréstimos ativos.")
                return
            print("Empréstimos ativos:")
            file.seek(0)  # Volta para o início do arquivo
            for row in reader:
                isbn, id_usuario, data_emprestimo = row
                print(f"Livro: {isbn}, Usuário: {id_usuario}, Data: {data_emprestimo}")
    except FileNotFoundError:
        print("Não há empréstimos ativos.")

# teste
associar_livro_usuario("3265456852445", "102", "2024-07-26")
associar_livro_usuario("3265456852445", "103", "2024-07-27")  # Tentativa de emprestar o mesmo livro
listar_emprestimos_ativos()
