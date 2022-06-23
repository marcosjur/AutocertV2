from flask import Flask, request, render_template, Response
from projects.create_cert import Certificate
from random import randint
from time import sleep

app = Flask(__name__)

@app.route('/', methods=['GET'])
def certificates_multi():
    return render_template("about_me.html")

""" @app.route('/autocert/single', methods=['POST'])
def certficates_single():
    
    payload = {'username':request.json['username'],
                'usercourse':request.json['usercourse'],
                'useremail':request.json['useremail'],
                'userid':request.json['userid']}
    
    user = Certificate(userid=payload['userid'], username=payload['username'], useremail=payload['useremail'], usercourse=payload['usercourse'])
    user.writing_certigicate()
    
    return Response(status=200, mimetype='application/json') """

@app.route('/karinacardoso', methods=['GET'])
def cardosin():
    return '<h1>Linda, te amo demais <3</h1>'


app.route('/test')
def tests():
    delay = randint(1,3)
    sleep(delay)
    r = f"<h1>Delay {delay}</h1>"
    return r
    
    


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=False)
