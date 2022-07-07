import os
import call_api
from flask import Flask, request, render_template, Response, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
@app.route("/index", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/autocert_formulario")
def autocert_form():
    return render_template("autocert_form.html")

@app.route("/autocert_formulario", methods=['POST','GET'])
def autocert_form_handler():
    name = request.form['name']
    email = request.form['email']
    course = request.form['course']
    new_object = {
        'code':os.environ.get('AUTOCERT_API_TOKEN'),
        'name': name,
        'course': course,
        'email': email,
        'status': 'success'
    }
    try:
        call_api.backend_call(payload=new_object)
        return redirect(url_for('success'))
    except Exception as e:
        return Response(status=500, mimetype='application/json')
    

@app.route("/aboutme")
def about_me():
    return render_template("about_me.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=False)
