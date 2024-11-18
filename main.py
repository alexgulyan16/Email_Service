from flask import Flask, request
from flask_mail import Mail, Message 
   
app = Flask(__name__) 

# Written by: Alexandra Gulyan

# Code is adapted from "Flask-Mail" and "Sending Emails Using API in Flask-Mail"
# Source URL: https://pypi.org/project/Flask-Mail/
# Source URL: https://www.geeksforgeeks.org/sending-emails-using-api-in-flask-mail/
   
# configuration of mail 
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'email@gmail.com'
app.config['MAIL_PASSWORD'] = 'password' # Google app password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app) 


# Verifies that all the required attributes are included
def email_attributes_valid(email_json):
    if "subject" not in email_json:
        return False
    elif "recipient_address" not in email_json:
        return False
    elif "message" not in email_json:
        return False
    else:
        return True


@app.route("/")
def index():
    return "Navigate to /email to send an email."

   
# Sends an email from the address set in app.config['MAIL_USERNAME']
# subject: The subject of the email. (string, required)
# recipient_address = The email address of the recipient. (string, required)
# message = The body of the email. (string, required)
@app.route("/" + "email", methods=["POST"]) 
def send_email(): 
    # Gets content from the body of the request
    content = request.get_json()

    # Check that all the required attributes are provided in the request body
    if email_attributes_valid(content) is False:
            return {"Error": "The request body is missing at least one of the required attributes."}, 400

    # Set the email variables
    subject = content["subject"]
    recipient_address = content["recipient_address"]
    message = content["message"]

    sender_address = app.config['MAIL_USERNAME']

    try:
        # Send the email
        msg = Message( 
                    subject, 
                    sender = sender_address, 
                    recipients = [recipient_address] 
                    ) 
        msg.body = message
        mail.send(msg) 
        return {"Email sent to": recipient_address}, 200
    except:
        return {"Error": "Check your email credentials and try again."}, 401
   
if __name__ == '__main__': 
   app.run(host="127.0.0.1", port=8000, debug=True)
