from flask import Flask, render_template
from application import app 

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')