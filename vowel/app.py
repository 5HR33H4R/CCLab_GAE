from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "***"


def rv(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""

    for i in range(len(s)):
        if s[i] not in vowels:
            result = result + s[i]
    print(result)
    return (result)


@app.route("/")
def index():
    flash("Enter the word", "")
    return render_template("index.html")


@app.route("/removeVowels", methods=["POST"])
def removeVowels():
    word = request.form['input']
    res = "The word after removing the vowels:" + rv(word)
    print('Res: ', res)
    flash(res)
    return render_template("index.html")
