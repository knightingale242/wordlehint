from flask import Flask, render_template, url_for
from definition import definition_finder

##### Flask intialization #####
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    
    definition = definition_finder()
    return render_template('index.html', definition = definition)

if __name__ == "__main__":
    app.run(debug=True)