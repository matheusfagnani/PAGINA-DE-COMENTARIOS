from flask import Flask,render_template,request,redirect
import datetime
from data.conexão import Conexao
from model.controler_mensagem import Mensagem
from model.controller_usuario import Usuario
app = Flask(__name__)
app.secret_key="periculoso"

#rotas do site

@app.route("/cadastro_usuario")
def pagina_cadastro_usuario():
    return render_template("tela_usuario.html")



@app.route("/login")
def pagina_de_login():
    return render_template("login.html")





@app.route("/post/logar",methods =["POST"])
def post_logar():
    usuario = request.form.get("login")
    senha=request.form.get("senha")
    esta_logado= Usuario.logar(usuario,senha)
    if esta_logado:
        return("/comentario")
    else:
       return redirect("/login")

@app.route("/post/cadastro_usuario", methods = ["POST"])
def post_cadastrar_usuario():
    nome= request.form.get("nome")
    usuario= request.form.get("usuario")
    senha= request.form.get("senha")

    usuario.cadastrar(usuario,senha,nome)
    return redirect("/comentario")

@app.route("/comentario")

def home_page():

    return render_template("comentarios.html")


@app.route("/logoff")   



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