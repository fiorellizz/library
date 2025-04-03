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

def cadastrar_livro(lista_livros, lenLista):
    livro = {}
    livro['id'] = lenLista + 1
    livro['titulo'] = input('Digite o nome do livro: ')
    livro['autor'] = input('Digite o nome do autor: ')
    livro['anoPublicacao'] = int(input('Digite o ano de publicação: '))
    livro['isbn'] = input('Digite a ISBN: ')
    livro['categoria'] = input('Digite o nome da categoria: ')
    lista_livros.append(livro)
    print('\nLivro cadastrado com sucesso!')
    return lista_livros

def listar_livros(lista_livros):
    if not lista_livros:
        print("Nenhum livro cadastrado.")
        return
    
    print("\n=== LISTA DE LIVROS ===")
    for i, livro in enumerate(lista_livros, 1):
        print(f"\nLivro {i}:")
        for chave, valor in livro.items():
            print(f"{chave.capitalize()}: {valor}")

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
        for i, livro in enumerate(resultados, 1):
            print(f"\nResultado {i}:")
            for chave, valor in livro.items():
                print(f"{chave.capitalize()}: {valor}")

def main():
    lista_livros = []
    lista_usuarios = []  
    emails_cadastrados = set()
    
    # ler arquivos csv caso existam e preencher a lista

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cadastrar novo livro")
        print("2 - Listar todos os livros")
        print("3 - Buscar livros")
        print("4 - Cadastrar usuário")
        print("5 - Listar usuários")
        print("0 - Sair")
        
        option = int(input("Digite a sua escolha: "))
        
        if option == 1:
            lista_livros = cadastrar_livro(lista_livros, len(lista_livros))
        elif option == 2:
            listar_livros(lista_livros)
        elif option == 3:
            buscar_livros(lista_livros)
        elif option == 4:
            lista_usuarios = cadastrar_usuario(emails_cadastrados, lista_usuarios)
        elif option == 5:
            listar_usuarios(lista_usuarios)
        elif option == 0:
            print(lista_livros)
            print(lista_usuarios)
            print(emails_cadastrados)
            # salvar nos arquivos csv as listas
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()