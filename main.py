
livros = []


def cadastrarLivro ():
    titulo = input("Titulos:  ")
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
  

def menu ():
    print("=" * 30)
    print ('Sistema de Biblioteca')
    print("=" * 30)
    print ('1 - Cadastrar Livros')
    print ('2 - Listar Livros')
    print("3 - Buscar Livros")
    print("4 - Remover Livros")
    print("0 - Sair")


while True:

    menu ()
    opcao = input("\n Escolha uma opção: ")

    if opcao == "1":
        cadastrarLivro()

    elif opcao == "2":
        print("\n🚧 Função ainda não implementada.\n")

    elif opcao == "3":
        print("\n🚧 Função ainda não implementada.\n")

    elif opcao == "4":
        print("\n🚧 Função ainda não implementada.\n")

    elif opcao == "0":
        print("\nPrograma encerrado!")
        break

    else:
        print("\n❌ Opção inválida!\n")




