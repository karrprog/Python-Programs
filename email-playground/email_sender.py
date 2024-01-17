import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Nathaniel Karr'
email['to'] = 'nathanielkarr81@live.com'
email['subject'] = 'Hey What\'s up'

email.set_content('I am a Python Master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('username', 'password')
    smtp.send_message(email)
    print('all good, message sent')