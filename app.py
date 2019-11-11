from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/formsubmission', methods = ['POST'])
def form_submission():
    qty = request.form.getlist("qty")
    return render_template('formsubmission.html',qty=qty)
