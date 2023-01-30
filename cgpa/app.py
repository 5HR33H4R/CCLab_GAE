from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "***"


@app.route("/")
def index():
    flash("Enter the values")
    return render_template("index.html")


@app.route("/cgpa", methods=["POST"])
def cgpa():
    numerator = 0
    denominator = 0
    for i in range(1, 9):
        gpa = 0
        credits = 0
        name1 = 'sem'+str(i)+'_gpa'
        name2 = 'sem'+str(i)+'_credits'
        if (request.form[name1] != ''):
            gpa = float(request.form[name1])
        if (request.form[name2] != ''):
            credits = float(request.form[name2])
        numerator += (gpa*credits)
        denominator += credits
    result = numerator/denominator
    res = "{0:.3f}".format(result)
    flash("Your CGPA is "+res)
    return render_template("index.html")
