import sqlite3

conexao = sqlite3.connect("biblioteca.db")  

conexao.row_factory = sqlite3.Row

cursor = conexao.cursor()

def criar_tabela():

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            titulo TEXT NOT NULL,

            autor TEXT NOT NULL,

            ano INTEGER NOT NULL

        )
    """)

    conexao.commit()
    
