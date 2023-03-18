from flask import Flask, render_template, url_for
# import tools


app = Flask(__name__)

@app.route("/")
def root():
    return render_template("template.html")
    # return render_template("base.html", names=..., arten=...)

if __name__ == "__main__":
    app.run(debug=True, port=55557, host="0.0.0.0")