from flask import Flask,render_template,request,redirect
import datetime
from data.conexão import Conexao
from model.controler_mensagem import Mensagem
app = Flask(__name__)

#rotas do site

@app.route("/cadastro_usuario")

@app.route("/comentario")

def home_page():
    return render_template("comentarios.html")



@app.route("/post/cadastrar_mensagem", methods = ["POST"])

def post_mensagem():
    usuario = request.form.get("usuario")
    mensagem =request.form.get("comentario")
   #cadastrando a mensagem usando a classe menssagem 
    Mensagem.cadastrar_mensagem(usuario,mensagem)
    return redirect("/comentario")

@app.route("/delete/mensagem/<codigo>")
def delete_mensagem(codigo):
    Mensagem.deletar_mensagen(codigo)
    return redirect ("/comentario")


@app.route("/put/mensagem/add/curtida/codigo")
def add_curtida(codigo):
    return redirect("/comentario")




app.run()