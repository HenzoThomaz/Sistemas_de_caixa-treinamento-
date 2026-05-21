import mysql.connector
from mysql.connector import Error

def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="estoque_sistema_caixa"
        )
        if conexao.is_connected():
            return conexao
    
    except Error as e:
        print(f"Aconteceu um erro inesperado, {e}")
        return None