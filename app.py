from flask import Flask
# from flask_mailman import Mail , Message 
from flask_mail import Mail , Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'mulumbamoses94@gmail.com'
app.config['MAIL_PASSWORD'] = 'ssij ndbc jxde pirw'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def index():

    msg = Message('Trial',  sender='mulumbamoses94@gmail.com', recipients=['mulumba.moses@stud.umu.ac.ug'])
    msg.body = "Hello there, Its Mhoses linum here trying out flask-mail"
    mail.send(msg)
    return 'Email sent succefully!'


if __name__ == '__main__':
    app.run(debug=True)
    