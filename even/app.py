from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "***"


@app.route("/")
def index():
    flash("Enter the value of N:")
    return render_template("index.html")


@app.route("/even", methods=["POST"])
def even():
    n = request.form['input']
    if n != '' and n.isdigit():
        n = int(n)
    else:
        n = 0
    res = ''
    limit = n
    for i in range(1, n+1):
        res += str(i*2) + ', '
    flash(f"The first {limit} Even Numbers are: ")
    return render_template("index.html", result=res[:-2])
