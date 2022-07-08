import os
import uuid
from projects.send_email import SendMail

class Certificate:
    
    def __init__(self, username=str, usercourse=str, useremail=str):
        self.username = username
        self.usercourse = usercourse
        self.useremail = useremail

        
    def writing_certificate(self):
        
                
        with open('projects/template/certificate_template.html', 'r+') as template:
            certificate_template = template.read()
            certificate_render = certificate_template.replace('{username}', self.username).replace('{usercourse}', self.usercourse)
            SendMail(cert=certificate_render, receiver=self.useremail).send()
        
        #Blob.upload(filename=filename, filepath=filepath)
        return
    