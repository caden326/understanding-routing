from flask import Flask  
app = Flask(__name__)    


@app.route('/')          
def hello_world():
    return 'Hello World!'  


@app.route('/dojo')          
def dojo():
    return 'dojo'


@app.route('/say/<string>')
def hi(string):
    print(string)
    return "Hi, " + string



@app.route('/repeat/<int:num>/<string:word>')
def num(num, word):
    result = word * num
    return result

@app.errorhandler(404)
def invalid(e):
    return "I dont have a response for you"



if __name__=="__main__":   
        app.run(debug=True)   

