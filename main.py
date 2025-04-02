from function import *
from menu import *
from variables import *

isRun = True

while isRun:
    painel()
    option = int(input("Digite sua escolha: "))
    if option == 1:
        cadastar()
    elif option == 2:
        listar_livros()
    elif option == 3:
        buscar_livro()
    elif option == 0:
        isRun = False