def grava_arquivo(type, dados):
    tipo = type.casefold()
    if tipo == "livro":    
        arquivo = open("biblioteca.csv","a")
 
        arquivo.write(f"{dados}" +"\n")

        arquivo.close()
        return
    elif tipo == "usuario":
        arquivo = open("usuarios.csv","a")

        arquivo.write(f"{dados}" +"\n")

        arquivo.close()
        return
    elif tipo == "emprestimo":
        arquivo = open("emprestimos.csv","a")

        arquivo.write(f"{dados}" +"\n")
        
        arquivo.close()
        return
    elif tipo == "categoria":
        arquivo = open("categorias.csv","a")
        
        arquivo.write(f"{dados}" +"\n")

        arquivo.close()
        return        
    elif tipo == "autor":
        arquivo = open("autor.csv","a")
   
        arquivo.write(f"{dados}" +"\n")
 
        arquivo.close()
        return

#iclusão do metodo para ler o arquivo e realizar a listagem e busca dos dados
def ler_arquivo(type):
    tipo = type.casefold() #CASEFOLD evita o case sensitive para não da erro nas buscas
    nome_arquivo = ""

    # para caso precise utilizar o metodo nos outros arquivos
    if tipo == "livro":
        nome_arquivo = "biblioteca.csv"
    elif tipo == "usuario":
        nome_arquivo = "usuarios.csv"
    elif tipo == "emprestimo":
        nome_arquivo = "emprestimos.csv"
    elif tipo == "categoria":
        nome_arquivo = "categorias.csv"
    elif tipo == "autor":
        nome_arquivo = "autor.csv"
    else:
        print("Tipo de arquivo inválido!")
        return []

    try:
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
            dados = [eval(linha.strip()) for linha in linhas]  # Converte string para dicionário
        return dados
    except FileNotFoundError: 
        return []
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return []

# apenas teste
# livro = {"Titulo":"o Livro","Autor":"Mano douglas","Ano_publicacao":"2015","ISBN":"3265456852445","Categoria":"comedia"}
# livro2 = {"Titulo":"o Livro2","Autor":"Maninho douglas","Ano_publicacao":"2016","ISBN":"3265456852449","Categoria":"acao"}

# grava_arquivo("categoria",livro2)