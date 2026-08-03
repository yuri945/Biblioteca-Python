from database import criar_tabela, cursor, conexao
from services import (
    cadastrarLivro,
    listarLivros,
    buscarLivro,
    removerLivro,
    editarLivro
)

from menu import menu

criar_tabela()


while True:

    menu ()
    opcao = input("\n Escolha uma opção: ")

    if opcao == "1":
        cadastrarLivro()

    elif opcao == "2":
        listarLivros()

    elif opcao == "3":
        buscarLivro()

    elif opcao == "4":
        removerLivro()

    elif opcao == "5":
        editarLivro()

    elif opcao == "0":
        print("\nPrograma encerrado!")
        break

    else:
        print("\n❌ Opção inválida!\n")




