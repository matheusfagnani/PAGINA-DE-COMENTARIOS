
from hashlib import sha256
from data.conexão import Conexao


class usuario :

    def cadastrar(usuario,senha,nome ):
        senha+sha256(senha.encode().hexdigest())


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



def logar(usuario,senha):
 
    senha+sha256(senha.encode().hexdigest())
    conexao = Conexao.criar_conexao()
    cursor = conexao.cursor()
    sql="""  select*from tb_usuario
    where login = %s 
    AND binary = "%s;   """
    valores=(usuario,senha)
    cursor.execute(sql,valores)
    resultado= cursor.fetchone
    conexao.commit()
#fechando a conexão 
    cursor.close()
    conexao.close()


