from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/payment')
def payment():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
    
@app.route('/about')
def about():
    return render_template('about.html')
