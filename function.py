import os, csv
from menu import menu_cadastros, menu_listagens

def cadastrar_usuario(emails_cadastrados, lista_usuarios):
    print("\n--- CADASTRO DE USUÁRIO ---")
    
    nome = input("Nome: ")
    email = input("E-mail: ")
    
    if email in emails_cadastrados:
        print("Erro: Este e-mail já está cadastrado!")
        return
    
    tipo = input("Tipo (aluno/professor/visitante): ").lower()
    while tipo not in ['aluno', 'professor', 'visitante']:
        print("Tipo inválido! Digite aluno, professor ou visitante")
        tipo = input("Tipo (aluno/professor/visitante): ").lower()
    
    id_unico = len(lista_usuarios) + 1
    
    usuario = {
        'id': id_unico,
        'nome': nome,
        'email': email,
        'tipo': tipo
    }
    
    lista_usuarios.append(usuario)
    emails_cadastrados.add(email)
    print("\nUsuário cadastrado com sucesso!")
    return lista_usuarios

def listar_usuarios(lista_usuarios):
    print("\n--- LISTA DE USUÁRIOS ---")
    if not lista_usuarios:
        print("Nenhum usuário cadastrado.")
        return
    
    for usuario in lista_usuarios:
        print(f"\nID: {usuario['id']}")
        print(f"Nome: {usuario['nome']}")
        print(f"E-mail: {usuario['email']}")
        print(f"Tipo: {usuario['tipo'].capitalize()}")

def cadastrar_livro(lista_livros):
    id_unico = len(lista_livros) + 1
    livro = {}
    livro['id'] = id_unico
    livro['titulo'] = input('Digite o nome do livro: ')
    livro['autor'] = input('Digite o nome do autor: ')
    livro['anoPublicacao'] = input('Digite o ano de publicação: ')
    
    while True:
        isbn = input('Digite a ISBN: ')
        if any(livro.get('isbn') == isbn for livro in lista_livros):
            print('Erro: Já existe um livro com esta ISBN. Por favor, insira um valor único.')
        else:
            livro['isbn'] = isbn
            break
    
    livro['categoria'] = input('Digite o nome da categoria: ')
    lista_livros.append(livro)
    print('\nLivro cadastrado com sucesso!')
    
    return lista_livros

def cadastrar_autor(lista_autores):
    id_unico = len(lista_autores) + 1
    autor = {}
    autor['id'] = id_unico
    autor['nome'] = input('Digite o nome do autor: ')
    
    while True:
        orcid = input('Digite o ORCID do autor: ')
        if any(autor.get('orcid') == orcid for autor in lista_autores):
            print('Erro: Já existe um autor com este ORCID. Por favor, insira um valor único.')
        else:
            autor['orcid'] = orcid
            break
    
    lista_autores.append(autor)
    print('\nAutor cadastrado com sucesso!')
    
    return lista_autores

def cadastrar_categoria(lista_categorias):
    id_unico = len(lista_categorias) + 1
    categoria = {}
    categoria['id'] = id_unico
    
    while True:
        nome = input('Digite o nome da categoria: ')
        if any(cat.get('nome') == nome for cat in lista_categorias):
            print('Erro: Já existe uma categoria com este nome. Por favor, insira um nome único.')
        else:
            categoria['nome'] = nome
            break
    
    lista_categorias.append(categoria)
    print('\nCategoria cadastrada com sucesso!')
    return lista_categorias

def listar_livros(lista_livros):
    if not lista_livros:
        print("Nenhum livro cadastrado.")
        return
    
    print("\n=== LISTA DE LIVROS ===")
    for livro in lista_livros:
        print(f"\nID: {livro['id']}")
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano de Publicação: {livro['anoPublicacao']}")
        print(f"ISBN: {livro['isbn']}")
        print(f"Categoria: {livro['categoria']}")

def listar_autores(lista_autores):
    if not lista_autores:
        print("Nenhum autor cadastrado.")
        return
    
    print("\n=== LISTA DE AUTORES ===")
    for autor in lista_autores:
        print(f"\nID: {autor['id']}")
        print(f"Nome: {autor['nome']}")
        print(f"ORCID: {autor['orcid']}")

def listar_categorias(lista_categorias):
    if not lista_categorias:
        print("Nenhuma categoria cadastrada.")
        return
    
    print("\n=== LISTA DE CATEGORIAS ===")
    for categoria in lista_categorias:
        print(f"\nID: {categoria['id']}")
        print(f"Nome: {categoria['nome']}")

def buscar_livros(lista_livros):
    if not lista_livros:
        print("Nenhum livro cadastrado para buscar.")
        return
    
    print("\nOpções de busca:")
    print("1 - Por Título")
    print("2 - Por Autor")
    print("3 - Por Categoria")
    
    opcao = int(input("Escolha o tipo de busca (1-3): "))
    termo = input("Digite o termo de busca: ").lower()
    
    resultados = []
    if opcao == 1:
        resultados = [livro for livro in lista_livros if termo in livro['titulo'].lower()]
    elif opcao == 2:
        resultados = [livro for livro in lista_livros if termo in livro['autor'].lower()]
    elif opcao == 3:
        resultados = [livro for livro in lista_livros if termo in livro['categoria'].lower()]
    else:
        print("Opção inválida!")
        return
    
    if not resultados:
        print("Nenhum livro encontrado.")
    else:
        print("\n=== RESULTADOS DA BUSCA ===")
        for livro in resultados:
            print(f"\nID: {livro['id']}")
            print(f"Título: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Categoria: {livro['categoria']}")

def realizar_emprestimo(lista_livros, lista_usuarios, lista_emprestimo):
    print("\n--- REALIZAR EMPRÉSTIMO ---")
    
    if not lista_livros or not lista_usuarios:
        print("Erro: É necessário ter livros e usuários cadastrados para realizar empréstimos.")
        return lista_emprestimo
    
    listar_livros(lista_livros)
    livro_id = int(input("\nDigite o ID do livro a ser emprestado: "))
    
    listar_usuarios(lista_usuarios)
    usuario_id = int(input("\nDigite o ID do usuário que está pegando o livro: "))
    
    emprestimo = {
        'id_livro': livro_id,
        'id_usuario': usuario_id,
        'data_emprestimo': input("Data do empréstimo (DD/MM/AAAA): "),
        'data_devolucao': input("Data prevista para devolução (DD/MM/AAAA): ")
    }
    
    lista_emprestimo.append(emprestimo)
    print("\nEmpréstimo realizado com sucesso!")
    return lista_emprestimo

def grava_arquivos(lista_autores, lista_categorias, lista_emprestimo, lista_livros, lista_usuarios, emails_cadastrados):
    arquivos = {
        'autores.csv': lista_autores,
        'categorias.csv': lista_categorias,
        'emprestimos.csv': lista_emprestimo,
        'livros.csv': lista_livros,
        'usuarios.csv': lista_usuarios,
        'emails.txt': emails_cadastrados
    }
    
    for nome_arquivo, dados in arquivos.items():
        try:
            if nome_arquivo.endswith('.csv'):
                with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
                    if dados:
                        writer = csv.DictWriter(arquivo, fieldnames=dados[0].keys())
                        writer.writeheader()
                        writer.writerows(dados)
            elif nome_arquivo == 'emails.txt':
                with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                    for email in dados:
                        arquivo.write(email + '\n')
        except Exception as e:
            print(f"Erro ao gravar {nome_arquivo}: {e}")

def ler_arquivos(lista_autores, lista_categorias, lista_emprestimo, lista_livros, lista_usuarios, emails_cadastrados):
    arquivos = {
        'autores.csv': lista_autores,
        'categorias.csv': lista_categorias,
        'emprestimos.csv': lista_emprestimo,
        'livros.csv': lista_livros,
        'usuarios.csv': lista_usuarios,
        'emails.txt': emails_cadastrados
    }
    
    for nome_arquivo, lista in arquivos.items():
        try:
            if os.path.exists(nome_arquivo):
                if nome_arquivo.endswith('.csv'):
                    with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo:
                        reader = csv.DictReader(arquivo)
                        for linha in reader:
                            linha_convertida = {}
                            for chave, valor in linha.items():
                                if chave == 'id':
                                    linha_convertida[chave] = int(valor)
                                else:
                                    linha_convertida[chave] = valor
                            lista.append(linha_convertida)
                elif nome_arquivo == 'emails.txt':
                    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                        for linha in arquivo:
                            email = linha.strip()
                            if email:
                                emails_cadastrados.add(email)
        except Exception as e:
            print(f"Erro ao ler {nome_arquivo}: {e}")

def cadastros(lista_livros, lista_usuarios, lista_autores, lista_categorias, emails_cadastrados):
    while True:
        menu_cadastros()
        opcao = int(input("Digite a sua escolha: "))
        
        if opcao == 1:
            lista_livros = cadastrar_livro(lista_livros)
        elif opcao == 2:
            lista_usuarios = cadastrar_usuario(emails_cadastrados, lista_usuarios)
        elif opcao == 3:
            lista_autores = cadastrar_autor(lista_autores)
        elif opcao == 4:
            lista_categorias = cadastrar_categoria(lista_categorias)
        elif opcao == 0:
            break
        else:
            print("Opção inválida! Tente novamente.")
    
    return lista_livros, lista_usuarios, lista_autores, lista_categorias

def listagens(lista_livros, lista_usuarios, lista_autores, lista_categorias):
    while True:
        menu_listagens()
        opcao = int(input("Digite a sua escolha: "))
        
        if opcao == 1:
            listar_livros(lista_livros)
        elif opcao == 2:
            listar_usuarios(lista_usuarios)
        elif opcao == 3:
            listar_autores(lista_autores)
        elif opcao == 4:
            listar_categorias(lista_categorias)
        elif opcao == 0:
            break
        else:
            print("Opção inválida! Tente novamente.")