#!/usr/bin/env python3
from flask import Flask , render_template, send_from_directory, abort, url_for, redirect
import werkzeug, os, git

repo = git.Repo('.')

app = Flask(__name__)


'''
Main script for the website of Joachim Hofmann

Functions in files:
- main.py:
    - routing of requests via flask
    - returning HTML files with jinja2 arguments
    - serving these files to the user

- requirements.txt
    - text file for all required Python modules for easy installation

- app.ini
    - Init file for an uwsgi server (with arguments)

- styles.css
    - CSS file for shared styles

- templates folder:

    - base.html
    - base template for the webpage
    - including JS functions for e.g. the darkmode
    - CSS stylings

    - index.html
        - the main page including building up the list of directories

    - dir.html
        - template for building up the list of directory contents
        - navigation buttons, current location listing

- static folder:

    - assets folder:
        - Icons used on the pages

    - files folder:
        - All files to be served as content on the page


Setup:
- install all required dependencies via
$ pip install -r requirements.txt

- This script is meant to be running on an uWSGI server, preferrably behind nginx.
    Quickstart docs: https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html
    nginx docs: https://www.nginx.com/resources/wiki/start/topics/tutorials/install/


- Paste into the nginx config file (/etc/nginx/sites-enabled/YOUR_SITE.conf):

    location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:3031;
    }

- Now add uwsgi to the services started at boot (Ubuntu uses Systemd, so the docs are at https://uwsgi-docs.readthedocs.io/en/latest/Systemd.html)

- Use certbot to get a free Let'sEncrypt SSL certificate
    Docs: https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal
    - Certbot automatically refreshes the certificate when it expires.


Testing the website locally:
- install all required dependencies via
$ pip install -r requirements.txt

- Testing after this step is easy, just run this python script and open up http://127.0.0.1:5000 in your browser.

'''

@app.route("/")
def home() :
    path = f"{os.getcwd()}/static/files/".replace("\\", "/")
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


@app.route("/<link>/<file>")
def folder(link, file) :

    href = f"{link}*{file}"
    path = f"{os.getcwd()}/static/files/".replace("\\", "/")
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

@app.route("/datenschutz")
def datenschutz():
    return render_template("datenschutz.html")

@app.route("/about")
def about():
    return render_template("about.html")

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
