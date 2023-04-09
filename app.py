import pyrebase
config = {
    "apiKey": "AIzaSyAR0XBuGC2yywq-q1DfQKfLl26LKk6l9K8",
  "authDomain": "fir-try-28f01.firebaseapp.com",
  "databaseURL": "https://fir-try-28f01-default-rtdb.firebaseio.com",
  "projectId": "fir-try-28f01",
  "storageBucket": "fir-try-28f01.appspot.com",
  "messagingSenderId": "588321601903",
  "appId": "1:588321601903:web:e072797fc9189e9465d09a",
  "measurementId": "G-04938M5W17"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
from flask import Flask,render_template,request, session
from flask_session import Session
import jinja2
app = Flask(__name__)
app.secret_key = 'secret'
@app.route('/')
@app.route('/index', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = email
            return render_template('home.html')
        except:  
                return 'failed to login'
    return render_template('index.html')

@app.route('/abc', methods = ['GET', 'POST'])
def abc():
    return render_template('create_account.html')

@app.route('/create_account', methods = ['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        pass1 = request.form['pass1']
        pass2 = request.form['pass2']
        if pass1 == pass2:
            if pass1:
                email = request.form['email']
                password = request.form['pass1']
                new_user = auth.create_user_with_email_and_password(email, password)
                auth.send_email_verification(new_user['idToken'])
                return render_template('verify_email.html')
            else:
                existing_account = "This Email id has already been used"
                return render_template('create_account.html', exist_msg=existing_account)

if __name__ == '__main__':
    app.run(debug=True, port=8000)