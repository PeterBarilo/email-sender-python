import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'NAME'
email['to'] = 'EMAIL'
email['subject'] = 'Test Email'

email.set_content(html.substitute({'name': 'Joe'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('EMAIL', 'PASS')
    smtp.send_message(email)
    print('Sent')


