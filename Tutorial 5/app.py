### Building Url Dynamically 
####Variable Rules And URL Building

from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my Youtube Channel'

@app.route('/success/<int:score>')
def success(score):
    return "<html><body><h1>The Reult is passed</h1></body></html>"


@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is "+ str(score)

### Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))


if __name__=='__main__':
    app.run(debug=True)