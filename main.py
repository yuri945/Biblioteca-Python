from database import criar_tabela

criar_tabela()

livros = []


def cadastrarLivro ():
    titulo = input("Titulo:  ")
    autor = input("Autor: ")
    ano = input("Ano: ")

    livro = {
        "titulo" : titulo,
        "autor" : autor,
        "ano" : ano
    }

    livros.append(livro)

    print("\n Livro cadastrado com sucesso! \n")


def listarLivros():
    if len(livros) == 0:
        print("\n Nenhum livro cadastrado até o momento.")

    else:
        print("\n=== LISTA DE LIVROS ===")
        for livro in livros:
            print(f"Titulo: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")
            print("-" * 30)



def buscarLivro(): 
    titulo = input("\n Digite o título do livro: ")

    encontrou = False

    for livro in livros:
        if livro["titulo"].lower() == titulo.lower():
            print("\n ----Livro Encontrado ----")
            print(f"Título: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")

            encontrou = True 
            break

    if not encontrou:
        print("\n Livro não listado no catálogo")


def removerLivro():
    titulo = input("\n Qual livro deseja remover?: ")

    encontrou = False

    for livro in livros:

        if livro["titulo"].lower() == titulo.lower():
            livros.remove(livro)

            print("\n Livro removido com sucesso!\n")

            encontrou = True
            break

    if not encontrou:
        print("\nLivro não listado no catálogo.\n ")


def editarLivro():
    titulo = input("\n Qual livro deseja editar?: ")

    encontrou = False

    for livro in livros:

        if livro["titulo"].lower() == titulo.lower():

            encontrou = True

            print("\nLivro encontrado!")
            print("1 - Título")
            print("2 - Autor")
            print("3 - Ano")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":

                novo_titulo = input("Novo título: ")
                livro["titulo"] = novo_titulo

            elif opcao == "2":

                novo_autor = input("Novo Autor: ")
                livro["autor"] = novo_autor

            elif opcao == "3":

                novo_ano = input("Novo ano: ")
                livro["ano"] == novo_ano

            else:
                print("Opção indisponível")
                return

            print("Livro atualizado com sucesso!")

        if not encontrou:
            print("Livro não encontrado")


def menu ():
    print("=" * 30)
    print ("Sistema de Biblioteca")
    print("=" * 30)
    print ("1 - Cadastrar Livros")
    print ("2 - Listar Livros")
    print("3 - Buscar Livros")
    print("4 - Remover Livros")
    print("5 - Editar Livros")
    print("0 - Sair")


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




