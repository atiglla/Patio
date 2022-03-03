from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", times=0)

@app.route("/play")
def play ():
    return render_template("index.html", times=3)

@app.route("/play/<int:numero>")
def varias (numero):
    return render_template("index.html", times=numero)




if __name__=="__main__":
    app.run(debug=True)