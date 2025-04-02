nomeAutor = ""
categoriaNome = ""

autorModelo = {
    "nome": nomeAutor
}

categoriaModelo = {
    "nome": categoriaNome
}

tituloLivro = ""
anoPublicacaoLivro = 0
isbnLivro = ""

livroModelo = {
    "titulo": tituloLivro,
    "autor": autorModelo["nome"],
    "anoPublicacao": anoPublicacaoLivro,
    "ISBN": isbnLivro,
    "categoria": categoriaModelo["nome"]
}

listaLivros = []

#criar o modelo para usuario e seus atributos