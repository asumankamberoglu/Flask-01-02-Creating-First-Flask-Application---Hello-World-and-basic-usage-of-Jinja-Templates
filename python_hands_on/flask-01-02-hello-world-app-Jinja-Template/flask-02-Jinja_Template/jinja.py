from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def head():
    return render_template("index.html", number1=8000, number2=2000)

@app.route("/sum")
def number():
    var1, var2 = 10000, 25000
    return render_template("body.html", num1 = var1, num2 = var2, sum =var1+var2)



if __name__== "__main__":
    app.run(debug=True)