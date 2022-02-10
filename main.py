#!/usr/bin/env python3
from flask import Flask , render_template, send_from_directory
import werkzeug
import os
import git

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

@app.route("/update")
def update():
    repo.remotes.origin.fetch()
    repo.remotes.origin.pull()
    return home()


@app.errorhandler(werkzeug.exceptions.NotFound)
def page_not_found(e):
    # note that we set the 404 status explicitly
    code = "404"
    description = "Page not found (go cry)-----"
    #dont make that ^^^^ longer than this ----|"
    return render_template('error.html', errcode= code, description= description), 404


if __name__ == "__main__":
    app.run(debug=True)
