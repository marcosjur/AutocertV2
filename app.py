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

@app.route("/autocert_formulario", methods=['POST','GET'])
def autocert_form_handler():
    name = request.form['name']
    email = request.form['email']
    course = request.form['course']
    try:
        Certificate(username=name, useremail=email, usercourse=course).writing_certificate()
        return render_template("success.html")
    except Exception as e:
        return Response(e, status=500, mimetype='application/json')
    

@app.route("/aboutme")
def about_me():
    return render_template("about_me.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=False)
