from flask import Flask, render_template, url_for

##### Flask intialization #####
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', omar=0)

if __name__ == "__main__":
    app.run(debug=True)