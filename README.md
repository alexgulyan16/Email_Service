# Email Service
This microservice is intended to be used with a gmail account. 

To send an email, send a POST request to http://127.0.0.1:5000/email  
The POST request should contain the subject, recipient_address, and message in the body of the request.

### Follow these steps before running the microservice:

1. Check that the gmail account is set up to use two-factor authentication
    - Manage google account -> Security -> 2-step verification
2. Create an app password
    - Manage google account -> Type “app password” into the search box 
    - Click on “app passwords” 
    - Type in a name for the app -> Click “create”
    - Copy the app password
3. Update the app.config['MAIL_PASSWORD'] string in main.py to the app password
4. Update the app.config['MAIL_USERNAME'] string to the gmail account email address

### To run:
1. Open your terminal and navigate to the folder containing main.py and requirements.txt
2. Create a virtual environment (optional):
    - python3 -m venv env
    - source env/bin/activate
3. Install dependencies:
    - pip install -r requirements.txt
4. Enter “python main.py” to run
5. Program will run at http://127.0.0.1:5000

## Communication Contract
### To send a request:

1. Check that the microservice is running at http://127.0.0.1:5000

2. Create a JSON object or dictionary containing 3 strings:
    - “subject”: The subject of the email. 
    - “recipient_address”: The recipient that will receive the email.    
    - “message”: The text that will be sent in the body of the email.

3. Send a POST request to  http://127.0.0.1:5000/email with the JSON object in the body of the request  

Example request (using python requests library):

```
email = {  
  "subject": "Hello!",  
  "recipient_address": "email@gmail.com",  
  "message": "Test email"  
}  
response = requests.post("http://127.0.0.1:5000/email", json=email)
```

### Data received:
If the email was successfully sent to the recipient, a 200 status code will be sent back as well as a JSON object containing the email address that the email was sent to.  

If one of the 3 attributes is missing from the request body, a 400 status code will be sent back as well as a JSON object containing an error message.  

If there are any other errors (most likely due to an authentication issue), a 401 status code will be sent back as well as a JSON object containing an error message.  

Viewing the data received:

```
print(response.json())
print("Status code:", response.status_code)
```

Result:
```
{'Email sent to': 'email@gmail.com'}
Status code: 200
```

### UML Sequence Diagram:
<img width="1303" alt="UML diagram" src="https://github.com/user-attachments/assets/f52ba2f4-fe52-45c6-a5c7-d7905ed21268">
