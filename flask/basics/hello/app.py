from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')    

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # Here you would typically process the data, e.g., save it to a database or send an email
        return render_template('home.html', name=name)
    return render_template('contact.html')

