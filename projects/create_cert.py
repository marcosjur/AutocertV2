import os
import uuid
from projects.upload_blob import Blob

class Certificate:
    
    def __init__(self, userid=int, username=str, usercourse=str, useremail=str):
        self.username = username
        self.usercourse = usercourse
        self.useremail = useremail
        self.userid = userid
        
    def writing_certigicate(self):
        
        filename = str(uuid.uuid4())+ ".html"
        pre_path = os.path.join("projects/certificates/", str(self.userid))
        filepath = os.path.join("projects/certificates/", str(self.userid), filename)
        
        try:
            os.mkdir(pre_path)
            print(f"Directory {pre_path} created!")
        except FileExistsError:
            print(f"Directory {pre_path} already exisits")
        
        with open('projects/template/certificate_template.html', 'r+') as template:
            certificate_template = template.read()
            certificate_render = certificate_template.replace('{username}', self.username).replace('{usercourse}', self.usercourse)
            certificate_final = open(filepath,"w")
            certificate_final.write(certificate_render)
            certificate_final.close()
        #Blob.upload(filename=filename, filepath=filepath)
        return
    