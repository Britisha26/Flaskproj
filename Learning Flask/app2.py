import json
from flask import Flask, redirect, render_template,request,url_for
app=Flask(__name__)
'''
Jinga Template Engine
{% for statements %}
{{ print output }}
{# #}

'''
@app.route('/')
def link():
    return "<a href='http://127.0.0.1:5000/hey'>Click Here to see if you can vote!</a>"



@app.route('/hey')
def hi():
    return render_template('htmapp2.html')


@app.route('/submit',methods=['GET', 'POST'])
def sub():
    x=request.form['n']
    y=request.form['a']
    y=str(y)

    if int(y)<18:
        vote="non"
        return redirect(url_for(vote,x=x,y=y))
    else:
        vote="oui"
        return redirect(url_for(vote,x=x,y=y))

@app.route('/non/<string:x>/<string:y>')
def non(x,y):
    #jsonify(j)
    return 'Dear ' +x+ " You are just " +y+ " You can't vote! Sorry!"

@app.route('/oui/<string:x>/<string:y>')
def oui(x,y):         
        return "Dear " +x+ " Congratulations! " +y+ " You're eligible to vote"


if __name__=='__main__':
    app.run(debug=True)

"""
    if int(y)<18:
        return 'Dear '+x+ " You can't vote! Sorry!"
    else:
        return  "Dear " +x+" You're eligible to vote"



"""