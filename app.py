from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from flask import send_file

app = Flask(__name__)
# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mapfumowesley27@gmail.com'
app.config['MAIL_PASSWORD'] = 'Chimedza2000!'


mail = Mail(app)

@app.route('/download_cv')
def download_cv():
    cv_file = 'static/MAPFUMO WESLEY --_CV.pdf'
    return send_file(cv_file, as_attachment=True, mimetype='application/pdf')

@app.route('/download_resume')
def download_resume():
    resume_file = 'static/MAPFUMO WESLEY RESUME..pdf'
    return send_file(resume_file, as_attachment=True, mimetype='application/pdf')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    mobile_number = request.form['mobile_number']
    subject = request.form['subject']
    message = request.form['message']

    if not name or not email or not mobile_number or not subject or not message:
        return 'Error: Please fill in all fields.'

    msg = Message(
        subject=subject,
        sender=email,
        recipients=['mapfumowesley27@gmail.com'],
        body=f"Name: {name}\nEmail: {email}\nMobile Number: {mobile_number}\nMessage: {message}"
    )

    try:
        mail.send(msg)
        return redirect(url_for('contacts'))
    except Exception as e:
        return 'Error sending email: {}'.format(str(e))

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == "__main__":
    app.run(debug=True)