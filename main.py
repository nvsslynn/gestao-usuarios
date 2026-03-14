from flask import Flask, redirect, url_for, render_template, request
import random
from localutil.jsonmanager import JSONManager

app = Flask(__name__)
dbpath = "database/users.json"
counterpath = "database/counter.json"

## HOME ##
@app.route("/")
def index():
    return render_template("home.html")
##########

## Criar
@app.route("/criar")
def panelcriar():
    return render_template("criar.html")

#
@app.route("/criar", methods=["POST"])
def criaraction():
    data = {
        "nome": request.form.get("nome"),
        "email": request.form.get("email")
    }
    user = {
        "nome": data["nome"],
        "email": data["email"]
    }
    
    fm = JSONManager(dbpath)
    fmf = fm.get()
    
    counter = JSONManager(counterpath)
    c = counter.get()
    sz = c["counter"]
    c["counter"] += 1
    counter.save(c)

    fmf[sz] = user
    fm.save(fmf)

    return redirect(url_for('index'))

############

# Apagar
@app.route("/apagar")
def panelapagar():
    return render_template("apagar.html")

@app.route("/apagar", methods=["POST"])
def apagaraction():
    fm = JSONManager(dbpath)
    data = fm.get()
    idu = request.form.get("idu")
    
    try:
        data.pop(idu)
    except:
        return render_template("error.html", error="Não existe!")

    fm.save(data)
    return redirect(url_for("index"))
############

# Editar
@app.route("/editar")
def paneleditar():
    return render_template('editar.html')
#
@app.route("/editar", methods=["POST"])
def editaraction():
    data = {
        "idu": request.form.get("idu"),
        "nome": request.form.get("nome"),
        "email": request.form.get("email")
    }
    idu = data["idu"]
    
    fm = JSONManager(dbpath)
    fmf = fm.get()

    try:
        xy = fmf[idu]
    except KeyError:
        return render_template("error.html", error="Usuário não existe")  

    usr = fmf[idu]
    
    if data["nome"]:
        usr["nome"] = data["nome"]
    if data["email"]:
        usr["email"] = data["email"]
    
    fmf[idu] = usr
    fm.save(fmf)

    return redirect(url_for('index'))
##############

@app.route("/ver")
def panelver():
    fm = JSONManager(dbpath)
    users = fm.get()

    return render_template("ver.html", users=users)

app.run(debug=True)