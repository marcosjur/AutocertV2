import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
import os

# enviando email
class SendMail:

    def __init__(self, receiver=str, cert=str):
        self.cert = cert
        self.anexo = Path(self.cert)
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.email = os.getenv('AUTOCERT_EMAIL_FROM')
        self.key = str(os.getenv('AUTOCERT_TOKEN_EMAIL'))
        self.msg = MIMEMultipart()
        self.email_destiny = receiver
        
        
        
    def send(self):
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login(self.email, self.key)

        # Mensage configuration
        self.msg["From"] = str(os.getenv('AUTOCERT_EMAIL_FROM'))
        self.msg["to"] = self.email_destiny
        self.msg["Subject"] = str(os.getenv('AUTOCERT_EMAIL_SUBJECT'))
        self.msg["Bcc"] = self.email_destiny

        # Send email
        self.msg.attach(MIMEText(self.cert, 'html'))
        
        # Drop the server
        self.server.send_message(self.msg)
        self.server.quit()
