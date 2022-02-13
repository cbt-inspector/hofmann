#!/usr/bin/env python3
from flask import Flask , render_template, send_from_directory, abort, url_for, redirect
import werkzeug, os, git

repo = git.Repo('.')

app = Flask(__name__)
filespath="static/files/"#relative paths start with the folder name, absolute paths with an /.


'''
Main script for the website of Joachim Hofmann
 -please read the README.md for mor informations

'''
# Haupt seite

if filespath[0]!="/":
    filespath=os.getcwd()+"/"+filespath

@app.route("/")
def home() :
    path = filespath.replace("\\", "/")
    dircontents = ["Klasse6","Klasse7","Klasse9","Klasse10","Klasse11","Klasse12","EngineAlpha"]
    fulllist = []
    for x in dircontents:
        bruh = f"{path}{x}"
        temp = os.listdir(bruh)
        if "Klasse" in x:
                sus = x.split("Klasse")
                temp.append(f"{sus[1]}. Jahrgangsstufe")
        elif x == "EngineAlpha":
                temp.append("EngineAlpha")
        fulllist.append(temp)
    return render_template("index.html", dircontents= fulllist)

# Ordner unter seiten
@app.route("/<link>/<file>")
def folder(link, file) :

    href = f"{link}*{file}"
    path = filespath.replace("\\", "/")
    npath = link.replace("*", "/")
    pth = npath
    if "JAHRGANGSSTUFE" in npath:
        sus = npath.replace("JAHRGANGSSTUFE","")
        npath = f"Klasse{sus}"
    elif npath.startswith("EngineAlpha"):
        npath = npath.replace("EngineAlpha", "EngineAlpha", 1)
    dircont = []
    fullpath = f"{path}{npath}/{file}"

    if "/" not in pth:
        pth = ""
    if "." in file:
        return send_from_directory(f"{path}{npath}", file, as_attachment= False)
    else:
        for x in os.listdir(fullpath):
            dircont.append(x)
        return render_template("dir.html", path = pth , cont= f"{npath}/{file}", dircont= dircont, href= href)
# Datenschutz seite
@app.route("/datenschutz")
def datenschutz():
    return render_template("datenschutz.html")
# Über uns seite
@app.route("/about")
def about():
    return render_template("about.html")
# Update funktions seite
@app.route("/update")
def update():
    repo.remotes.origin.fetch()
    repo.remotes.origin.pull()
    return redirect(url_for('home'))

# ERROR CODES    ///////////////////////////////////////////////////////////////
# ERROR CODES    ///////////////////////////////////////////////////////////////
# ERROR CODES    ///////////////////////////////////////////////////////////////
# ERROR CODES    ///////////////////////////////////////////////////////////////
# ERROR CODES    ///////////////////////////////////////////////////////////////
# ERROR CODES    ///////////////////////////////////////////////////////////////

@app.route("/testerror/<err>")
def testerror(err):
    abort(int(err))

@app.errorhandler(werkzeug.exceptions.BadRequest)
def BadRequest(e):
    code = 400
    description = f"{e}"
    return render_template('error.html', errcode= f"{code}", description= description), code

@app.errorhandler(werkzeug.exceptions.NotFound)
def NotFound(e):
    code = 404
    description = f"{e}"
    return render_template('error.html', errcode= f"{code}", description= description), code

@app.errorhandler(werkzeug.exceptions.RequestTimeout)
def RequestTimeout(e):
    code = 408
    description = f"{e}"
    return render_template('error.html', errcode= f"{code}", description= description), code

@app.errorhandler(werkzeug.exceptions.Gone)
def Gone(e):
    code = 410
    description = f"{e}"
    return render_template('error.html', errcode= f"{code}", description= description), code

@app.errorhandler(werkzeug.exceptions.RequestEntityTooLarge)
def RequestEntityTooLarge(e):
    code = 413
    description = f"{e}"
    return render_template('error.html', errcode= f"{code}", description= description), code

@app.errorhandler(werkzeug.exceptions.RequestURITooLarge)
def RequestURITooLarge(e):
    code = 414
    description = f"{e}"
    return render_template('error.html', errcode= f"{code}", description= description), code

@app.errorhandler(werkzeug.exceptions.UnsupportedMediaType)
def UnsupportedMediaType(e):
    code = 415
    description = f"{e}"
    return render_template('error.html', errcode= f"{code}", description= description), code

@app.errorhandler(werkzeug.exceptions.ImATeapot)
def ImATeapot(e):
    code = 418
    description = "418 I'm a teapot: The server refuses to brew coffee because it is, permanently, a teapot"
    return render_template('error.html', errcode= f"{code}", description= description), code

@app.errorhandler(werkzeug.exceptions.Locked)
def Locked(e):
    code = 423
    description = f"{e}"
    return render_template('error.html', errcode= f"{code}", description= description), code

@app.errorhandler(werkzeug.exceptions.TooManyRequests)
def TooManyRequests(e):
    code = 429
    description = f"{e}"
    return render_template('error.html', errcode= f"{code}", description= description), code

@app.errorhandler(werkzeug.exceptions.InternalServerError)
def InternalServerError(e):
    code = 500
    description = f"{e}"
    return render_template('error.html', errcode= f"{code}", description= description), code

@app.errorhandler(werkzeug.exceptions.BadGateway)
def BadGateway(e):
    code = 502
    description = f"{e}"
    return render_template('error.html', errcode= f"{code}", description= description), code

@app.errorhandler(werkzeug.exceptions.GatewayTimeout)
def GatewayTimeout(e):
    code = 504
    description = f"{e}"
    return render_template('error.html', errcode= f"{code}", description= description), code

@app.errorhandler(werkzeug.exceptions.HTTPVersionNotSupported)
def HTTPVersionNotSupported(e):
    code = 505
    description = f"{e}"
    return render_template('error.html', errcode= f"{code}", description= description), code


# RUN APP //////////////////////////////////////
# RUN APP //////////////////////////////////////
# RUN APP //////////////////////////////////////
# RUN APP //////////////////////////////////////
# RUN APP //////////////////////////////////////
# RUN APP //////////////////////////////////////
# RUN APP //////////////////////////////////////


if __name__ == "__main__":
    app.run(debug=True)
