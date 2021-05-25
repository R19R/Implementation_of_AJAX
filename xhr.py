from flask import Flask, redirect, render_template, request




app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/successjs", methods=['POST', 'GET'])
def successjs():
    if request.method == "POST":
        result = request.form
        username = request.form['name']
        return render_template("successjs.html", result=result, username=username)



if __name__ == "__main__":
    app.run(debug=True)
