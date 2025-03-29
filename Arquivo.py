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

# apenas teste
# livro = {"Titulo":"o Livro","Autor":"Mano douglas","Ano_publicacao":"2015","ISBN":"3265456852445","Categoria":"comedia"}
# livro2 = {"Titulo":"o Livro2","Autor":"Maninho douglas","Ano_publicacao":"2016","ISBN":"3265456852449","Categoria":"acao"}

# grava_arquivo("categoria",livro2)