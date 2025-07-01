from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Gmail SMTP Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'rohithaandey@gmail.com'
app.config['MAIL_PASSWORD'] = 'jyjanabjjtajbhkx'  # App password from Google
app.config['MAIL_DEFAULT_SENDER'] = 'rohithaandey@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        sender_name = request.form['name']
        sender_email = request.form['email']
        recipient_email = request.form['recipient']
        message_body = request.form['message']

        # Send email to the recipient entered by user
        msg = Message(
            subject=f"Message from {sender_name}",
            recipients=[recipient_email],  # ← Dynamic recipient
            body=f"{sender_name} ({sender_email}) sent you this message:\n\n{message_body}"
        )
        mail.send(msg)

        # Optional: Also notify you (Rohitha)
        admin_msg = Message(
            subject="📬 Contact Form Submission",
            recipients=["rohithaandey@gmail.com"],
            body=f"{sender_name} ({sender_email}) sent an email to {recipient_email}.\n\nMessage:\n{message_body}"
        )
        mail.send(admin_msg)

        return redirect(url_for('thankyou'))

    return render_template('contact.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
