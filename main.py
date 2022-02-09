from flask import Flask , render_template, send_from_directory
import os

app = Flask(__name__)




@app.route("/")
def home() :
    path = f"{os.getcwd()}/static/bruh/".replace("\\", "/")
    #tempcontents = os.listdir(path)
    #dircontents = []
    #for x in tempcontents:
    #    if "Klasse" in x:
    #        sus = x.split("Klasse")
    #        dircontents.append(f"{sus[1]}. Jahrgangsstufe")
    #    elif x == "EA":
    #        dircontents.append("Engine Alpha")
    #    else:
    #        dircontents.append(x)
    #dircontents.sort()
    dircontents = ["Klasse6","Klasse7","Klasse9","Klasse10","Klasse11","Klasse12","EA"]
    fulllist = []
    for x in dircontents:
        bruh = f"{path}{x}"
        temp = os.listdir(bruh)
        if "Klasse" in x:
                sus = x.split("Klasse")
                temp.append(f"{sus[1]}. Jahrgangsstufe")
        elif x == "EA":
                temp.append("Engine Alpha")
        fulllist.append(temp)
    #dircontents = ["6. Jahrgangsstufe","7. Jahrgangsstufe","9. Jahrgangsstufe","10. Jahrgangsstufe","11. Jahrgangsstufe","12. Jahrgangsstufe","Engine Alpha",]
    return render_template("index.html", dircontents= fulllist)


@app.route("/<link>/<file>")
def folder(link, file) :
    #contents= []
    #path = f"{os.getcwd()}/static/bruh/"
    #for x in [os.path.join(root, name).split(path)
    #         for root, dirs, files in os.walk(path)
    #         for name in files]:
    #             e= x[1].replace("\\","/")
    #             contents.append(e)
    #
    #dir_list = next(os.walk(path))[1]
    #
    #
    #return ''.join([f"{str(x)}-- " for x in dir_list])
    href = f"{link}*{file}"
    path = f"{os.getcwd()}/static/bruh/".replace("\\", "/")
    npath = link.replace("*", "/")
    pth = npath
    if "JAHRGANGSSTUFE" in npath:
        sus = npath.replace("JAHRGANGSSTUFE","")
        npath = f"Klasse{sus}"
    elif npath.startswith("EngineAlpha"):
        npath = npath.replace("EngineAlpha", "EA", 1)
    dircont = []
    fullpath = f"{path}{npath}/{file}"
    #for root, dirs, files in os.walk(f"{path}{npath}/{file}", topdown=True):
    #    for name in files:
    #        #if file not in root:
    #        dircont.append(name.replace("\\","/"))
    #    for name in dirs:
    #        #if file in root:
    #        dircont.append(name.replace("\\","/"))

    if "/" not in pth:
        pth = ""
    if "." in file:
        return send_from_directory(f"{path}{npath}", file, as_attachment= False)
    else:
        for x in os.listdir(fullpath):
            dircont.append(x)
        return render_template("dir.html", path = pth , cont= f"{npath}/{file}", dircont= dircont, href= href)


if __name__ == "__main__":
    app.run(debug=True)
