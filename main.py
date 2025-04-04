from function import buscar_livros, cadastros, grava_arquivos, ler_arquivos, listagens, realizar_emprestimo
from menu import menu_principal
from variables import *

def main():
    # Carregar dados dos arquivos
    ler_arquivos(lista_autores, lista_categorias, lista_emprestimo, lista_livros, lista_usuarios, emails_cadastrados)

    # Loop principal
    while True:
        menu_principal()
        opcao = int(input("Digite a sua escolha: "))
        
        if opcao == 1:  # Cadastros
            lista_livros, lista_usuarios, lista_autores, lista_categorias = cadastros(
                lista_livros, lista_usuarios, lista_autores, lista_categorias, emails_cadastrados
            )
        elif opcao == 2:  # Listagens
            listagens(lista_livros, lista_usuarios, lista_autores, lista_categorias)
        elif opcao == 3:  # Buscar Livro
            buscar_livros(lista_livros)
        elif opcao == 4:  # Empréstimo
            lista_emprestimo = realizar_emprestimo(lista_livros, lista_usuarios, lista_emprestimo)
        elif opcao == 0:  # Sair
            grava_arquivos(lista_autores, lista_categorias, lista_emprestimo, lista_livros, lista_usuarios, emails_cadastrados)
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()