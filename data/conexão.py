import mysql.connector
class Conexao:
    def criar_conexao():
        conexao= mysql.connector.connect(host="bdgodofredo-alexstocco-93db.b.aivencloud.com", 
                                        port=27974,
                                        user="3ds",
                                    password="banana",
                                    database="Cadastro_comentarios")
        return conexao