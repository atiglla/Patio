from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", times=1,color="aquamarine")

@app.route("/play")
def play ():
    return render_template("index.html", times=3,color="aquamarine")

@app.route("/play/<int:numero>")
def varias (numero):
    return render_template("index.html", times=numero)

@app.route("/play/<int:numero>/<y>")
def varias2 (numero,y):
    return render_template("index.html", times=numero, color=y)




if __name__=="__main__":
    app.run(debug=True)