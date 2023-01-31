from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "***"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/fahrenheit")
def fahrenheit():
    flash("Enter the Temperature:")
    return render_template("fahrenheit.html")


@app.route("/calcCelcius", methods=["POST"])
def calcCelcius():
    # flash("Hi " + str(request.form['name_input']) + ", Great to see you!")
    temp = int(request.form['f_input'])
    res = (temp - 32) * (5/9)
    flash("The Temperature in Celcius: "+"%.2f" % res)
    return render_template("fahrenheit.html")


@app.route("/celcius")
def celcius():
    flash("Enter the Temperature?")
    return render_template("celcius.html")


@app.route("/calcFahrenheit", methods=["POST"])
def calcFahrenheit():
    temp = int(request.form['c_input'])
    res = (temp * (9/5)) + 32
    flash("The Temperature in Fahrenheit: "+"%.2f" % res)
    return render_template("celcius.html")


if __name__ == "__main__":
    app.run()
