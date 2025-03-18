import datetime

from data.conexão import Conexao


class Mensagem :
 
 def cadastrar_mensagem(usuario,mensagem):
    data_hora= datetime.datetime.now()
    conexao = Conexao.criar_conexao()
    cursor = conexao.cursor(dictionary=True)
   # criando o sql
    sql= """INSERT INTO  tb_comentarios (
        "cod_comentario"
        nome,
        data_hora,
        comentario,) VALUES (%s,%s,%s)"""
    
    valores=(data_hora,usuario,mensagem)
    
    cursor.execute(sql,valores)
    conexao.commit()
#fechando a conexão 
    cursor.close()
    conexao.close()


def recuperar_mensagens():

    sql= """ SELECT data_hora,
    nomeas usuario,
    comentatios as mensagem 
    from  tb_comentarios () """
    conexao = Conexao.criar_conexao()
    cursor = conexao.cursor(dictionary=True)



    cursor.execute(sql)
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()
    
    return resultado


def deletar_mensagen(codigo):
    conexao = Conexao.criar_conexao()
    cursor = conexao.cursor(dictionary=True)
    
    sql= """ DELETE from tb_comentarios Where cod_comentario = %s; """
    valores= (codigo)
    cursor.execute(sql,valores)
    conexao.commit()

    cursor.close()
    conexao.close()

















