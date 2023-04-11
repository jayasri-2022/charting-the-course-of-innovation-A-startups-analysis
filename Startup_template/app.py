from flask import Flask,redirect,url_for,render_template

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html','about.html','contact.html','service.html','images','css','js','plugins','scss')

@app.route('/company')
def displaymycompany():
    return "Smart Bridge"