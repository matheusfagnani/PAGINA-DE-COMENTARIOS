import mysql.connector
class Conexao:
    def criar_conexao():
        conexao= mysql.connector.connect(host="10.110.134.2", 
                                        port=3306,
                                        user="root",
                                    password="root",
                                    database="Cadastro_comentarios")
        return conexao