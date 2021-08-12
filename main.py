from flask import Flask, render_template, request, redirect
from PIL import Image, ImageEnhance
import os

root = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

@app.route("/")
def editing():
    imgName = "a.jpg" 
    if os.path.isfile(root + "/static/img/edited_" + imgName):
        return render_template("main.html", img = "edited_" + imgName)
    return render_template("main.html", img = imgName)

@app.route("/rotate", methods = ["POST"])
def rotate():
    with Image.open(root + "/static/img/" + request.form["imgName"].replace("edited_", "")) as img:
        if "edited_" in request.form["imgName"]:
            img.rotate(int(request.form["angle"])).save(root + "/static/img/" + request.form["imgName"])
        else:
            img.rotate(int(request.form["angle"])).save(root + "/static/img/edited_" + request.form["imgName"])
    return redirect("/")

@app.route("/removeColor", methods = ["POST"])
def removeColor():
    with Image.open(root + "/static/img/" + request.form["imgName"].replace("edited_", "")) as img:
        if "edited_" in request.form["imgName"]:
            img.convert(mode="L").save(root + "/static/img/" + request.form["imgName"])
        else:
            img.convert(mode="L").save(root + "/static/img/edited_" + request.form["imgName"])
    return redirect("/")

@app.route("/reset", methods = ["POST"])
def reset():
    if "edited_" in request.form["imgName"] and os.path.isfile(root + "/static/img/" + request.form["imgName"]):
        os.remove(root + "/static/img/" + request.form["imgName"])
    return redirect("/")

@app.route("/a", methods=["POST"])
def a():
    with Image.open(root + "/static/img/" + request.form["imgName"].replace("edited_", "")) as img:
        enhancer = ImageEnhance.Contrast(img)
        if "edited_" in request.form["imgName"]:
            enhancer.enhance(float(request.form["factor"])).save(root + "/static/img/" + request.form["imgName"])
        else:
            enhancer.enhance(float(request.form["factor"])).save(root + "/static/img/edited_" + request.form["imgName"])
    return redirect("/")



app.run(debug=True)