from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Cams():
    return render_template("cams.html")

@app.route('/about')
def About():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True, port=1026)