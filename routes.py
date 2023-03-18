from flask import Flask, render_template, url_for
import tools


app = Flask(__name__)

@app.route("/")
def root():
    return render_template("template.html")
    # return render_template("base.html", names=..., arten=...)

@app.route("/usg")
def usg():
    return render_template("avgusagegmd.html")
    # return render_template("base.html", names=..., arten=...)

@app.route("/solar")
def solar():
    gmde = tools.getDataListSolar("stadt_name")
    januar = tools.getDataListSolar("januar")
    februar = tools.getDataListSolar("februar")
    maerz = tools.getDataListSolar("maerz")
    april = tools.getDataListSolar("april")
    mai = januar = tools.getDataListSolar("mai")
    juni = tools.getDataListSolar("juni")
    juli = tools.getDataListSolar("januar")
    august = tools.getDataListSolar("august")
    november = november = tools.getDataListSolar("januar")
    dezember = dezember = tools.getDataListSolar("januar")
    return render_template("solar.html", gmde=gmde, januar=januar, februar=februar, maerz=maerz, april=april, mai=mai, juni=juni, juli=juli, august=august, november=november, dezember=dezember)

@app.route("/minenergie")
def minenergy():
    gmde = tools.getDataListMinenergie("ort_name")
    minergie = tools.getDataListMinenergie("minergie")
    minergie_eco = tools.getDataListMinenergie("minergie_eco")
    minergie_a = tools.getDataListMinenergie("minergie_a")
    minergie_a_eco = tools.getDataListMinenergie("minergie_a_eco")
    minergie_p = tools.getDataListMinenergie("minergie_p")
    minergie_p_eco = tools.getDataListMinenergie("minergie_p_eco")
    return render_template("minenergie.html", gmde=gmde, minergie=minergie, minergie_eco=minergie_eco, minergie_a=minergie_a, minergie_a_eco=minergie_a_eco, minergie_p=minergie_p, minergie_p_eco=minergie_p_eco)

if __name__ == "__main__":
    app.run(debug=True, port=55555, host="0.0.0.0")