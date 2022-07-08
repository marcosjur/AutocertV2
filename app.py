from crypt import methods
import os
import json
from flask import Flask, request, render_template, Response, redirect, url_for
from projects.create_cert import Certificate

app = Flask(__name__)

@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
@app.route("/index", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/autocert_formulario", methods=['GET'])
def autocert_form():
    return render_template("autocert_form.html")

@app.route("/autocert_formulario", methods=['POST'])
def autocert_form_handler():
    name = request.form['name']
    email = request.form['email']
    course = request.form['course']
    
    Certificate(username=name, useremail=email, usercourse=course).writing_certificate()
    return render_template("success.html")
    

@app.route("/aboutme")
def about_me():
    return render_template("about_me.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=False)
