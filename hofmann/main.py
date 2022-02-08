from flask import Flask , render_template
import os

app = Flask(__name__)




@app.route("/")
def home() :
    #path = f"{os.getcwd()}/static/bruh/".replace("\\", "/")
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
    dircontents = ["6. Jahrgangsstufe","7. Jahrgangsstufe","9. Jahrgangsstufe","10. Jahrgangsstufe","11. Jahrgangsstufe","12. Jahrgangsstufe","Engine Alpha",]
    return render_template("index.html", dircontents= dircontents)


@app.route("/<bruh>")
def folder(bruh) :
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
    return bruh





if __name__ == "__main__":
    app.run(debug=True)
