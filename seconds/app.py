from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "***"


@app.route("/")
def index():
    flash("Enter the values", "")
    return render_template("index.html")


@app.route("/seconds", methods=["POST"])
def seconds():
    hrs = request.form['h_input']
    if hrs != '':
        hrs = int(hrs)
    else:
        hrs = 0
        min = 0
    min = request.form['m_input']
    if min != '':
        min = int(min)
    else:
        min = 0
    res = (min * 60) + (hrs * 3600)
    res = "Number of Seconds: " + str(res)
    print('Res: ', res)
    flash(res)
    return render_template("index.html")
