from flask import Flask, render_template, request, flash, redirect
from flask_mail import Mail, Message


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'k76922045@gmail.com'
app.config['MAIL_PASSWORD'] = 'jbfe msos qecg xnvh'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/location')
def location():
    return render_template('location.html')


@app.route('/membership', methods=['GET', 'POST'])
def membership():
    if request.method == 'POST':
        email = request.form['email']
        msg = Message("Hey", sender='k76922045@gmail.com', recipients=[email])
        msg.body = "Thank you for signing up for The Kitchen newsletter.\
              Have a free dessert next time you dine with us."
        mail.send(msg)
        return "Sent"
    return render_template('membership.html')


@app.route('/order')
def order():
    return render_template('order.html')


if __name__ == '__main__':
    app.run(debug=True)
