def sendEmail():
    import requests

    url = "https://free-email-sender.p.rapidapi.com/sendemail"

    querystring = {"senderEmail":"sender email address","password":"sender account password","email":"reciever's email","subject":"email subject","message":"message to be sent"}

    payload = {
        "senderEmail": "xyz@gmail.com",
        "password": "password",
        "email": "xyz@gmail.com",
        "subject": "Email Api checking",
        "message": "Hello Just for checking"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "f318e8573amsha7246f29e8d7de7p1c368fjsn5b4af82f4ba1",
        "X-RapidAPI-Host": "free-email-sender.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

    print(response.text)
    