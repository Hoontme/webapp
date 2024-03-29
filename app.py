from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')
@app.route('/homepage')
def homepage():
    return render_template('homePage.html')
@app.route('/name/<name>')
def name(name):
    return render_template('name.html',name=name)
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
