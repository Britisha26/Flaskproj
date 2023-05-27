from flask import Flask, redirect, url_for, request, render_template
app=Flask(__name__,template_folder='ecohtml')

@app.route('/')
def welcome():
    return render_template('ecowelcome.html')

@app.route('/srijith')
def srijith():
    return render_template("ecosrijith.html")

@app.route('/tisha')
def tisha():
    return render_template("ecotisha.html")

    
@app.route('/app')
def ap():
    return render_template("ecoapp.html")

@app.route('/mobileapp')
def moap():
    return render_template("ecomobileapp.html")

@app.route('/bin')
def bin():
    return render_template("ecobin.html")

@app.route('/form')
def form():
    return render_template("ecoform.html")

if __name__=='__main__':
    app.run(debug=True)