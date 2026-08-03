from database import cursor, conexao

def cadastrarLivro ():
    titulo = input("\nTitulo :")
    autor = input("Autor: ")
    ano = input("Ano: ")

    cursor.execute("""
    INSERT INTO livros (titulo, autor, ano)
    VALUES (?,?,?)
    """,(titulo, autor, ano))

    conexao.commit()

    print("\n Livro cadastrado com sucesso! \n")


def listarLivros():

    cursor.execute("SELECT * FROM livros")

    livros = cursor.fetchall()

    if len(livros) == 0:
        print("\n Nenhum livro cadastrado até o momento.")
        return

    print("\n===== LISTA DE LIVROS =====\n")


    for livro in livros:
        print(f"ID: {livro[0]}")
        print(f"Titulo: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano: {livro['ano']}")
        print("-" * 30)



def buscarLivro(): 

    titulo = input("\n Digite o título do livro: ")

    cursor.execute("""
    SELECT * FROM livros 
    WHERE titulo = ?
    """, (titulo,))

    livro = cursor.fetchone()

    if livro:
        print("\n===== LIVRO ENCONTRADO =====")

        print(f"ID: {livro[0]}")
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano: {livro['ano']}")
        print("-" * 30)

    else:
        print("\nLivro não encontrado.\n")

    

def removerLivro():
    titulo = input("\n Qual livro deseja remover?: ")

    cursor.execute("""
    SELECT * FROM livros
    WHERE titulo = ?
    """, (titulo,))

    livro = cursor.fetchone()

    if livro:

        cursor.execute("""
        DELETE FROM livros
        WHERE titulo = ?
        """, (titulo,))

        conexao.commit()

        print("\nLivro removido com sucesso!\n")

    else:
        print("\nLivro não encontrado\n")


def editarLivro():

    titulo = input("\n Qual livro deseja editar?: ")

    cursor.execute("""
    SELECT * FROM livros
    WHERE titulo = ?
    """, (titulo,))

    livro = cursor.fetchone()

    if not livro:
        print("\nLivro não encontrado\n")
        return

    print("\nLivro encontrado!")
    print("1 - Editar Título")
    print("2 - Editar Autor")
    print("3 - Editar Ano")

    opcao = input("\n Escolha uma opção: ")

    if opcao == "1":

        novo_titulo = input("Digite o novo titulo: ")

        cursor.execute ("""
        UPDATE livros
        SET titulo = ?
        WHERE titulo = ?
        """, (novo_titulo, titulo))

    elif opcao == "2":

        novo_autor = input("Digite o novo autor: ")

        cursor.execute ("""
        UPDATE livros
        SET autor = ?
        WHERE titulo = ?
        """, (novo_autor, titulo))

    elif opcao == "3":

        novo_ano = input("Digite o novo ano: ")

        cursor.execute ("""
        UPDATE livros
        SET ano = ?
        WHERE titulo = ?
        """, (novo_ano, titulo))

    else: 
        print("\nOpção Invalida\n")
        return

    conexao.commit()
    print("\nLivro atualizado com sucesso!\n")