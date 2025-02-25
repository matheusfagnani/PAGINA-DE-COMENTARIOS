from flask import Flask
app = Flask(__name__)

#rotas do site


@app.route("/")

def home_page():
    return "home_page"





app.run()