
from data.conexão import Conexao


class usuario :

    def cadastrar(usuario,senha,nome ):
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor()
   # criando o sql
        sql= """INSERT INTO  tb_cadastro_Usuario(
            usuario,
            senha,
            nome,
            ) VALUES (%s,%s,%s)"""
        
        valores=(usuario,senha,nome)
        
        cursor.execute(sql,valores)
        conexao.commit()
    #fechando a conexão 
        cursor.close()
        conexao.close()
