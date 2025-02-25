from flask import Flask,render_template,request,redirect
import datetime
import mysql.connector
app = Flask(__name__)

#rotas do site


@app.route("/")

def home_page():
    return render_template("comentarios.html")



@app.route("/post/cadastrar_mensagem", methods = ["POST"])

def post_mensagem():
    usuario = request.form.get("usuario")
    mensagem =request.form.get("comentario")
    data_hora= datetime.datetime.now()
    return redirect("/")




conexao= mysql.conector.conect(hostname="localhost", 
                                porta=3306,
                                user="root",
                               password="root",
                               database="Cadastro_comentarios")

cursor = conexao.cursor()

conexao.comit()

# criando o sql

sql= """INSERT INTO  tb_comentarios (
nome,data_hora,comentario) VALUES (%s,%s,%s)"""

valores=(usuario,mensagem,data_hora)

#fechando a conexão 
cursor.close()
conexao.close()



app.run()