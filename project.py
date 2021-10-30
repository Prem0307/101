import os
import dropbox 
from dropbox.files import WriteMode

class TransferData:
    def  __init__(self,access_token):
        self.access_token=access_token
    

    def upload_file(self,file_from,file_to):
         dbx=dropbox.Dropbox(self.access_token)
   

    for root,dirs,files in os.walk('file_from'):

        for filename in files:
            local_path=os.path.join(root,filename)
            relative_path=os.path.relpath(local_path,file_from)
            dropbox_path=os.path.join(file_to,relative_path)

            with open(local_path,'rb') as f:
                dbx.files_upload(f.read(),dropbox_path,mode.WriteMode('overwrite'))

    def main():
        access_token='sl.A7JUwvdcB7QqECIYlOOBWBZ92EVu2gyUaK5vMNSc515XR0S4f-oRPmpkU3HirxJkd6LvitCtzmhtujZ_2mEz6IgISZOChKLk3iIpZFFUJAQfLB5JphYhZKw2c4sPAaNJu3D0Af0Lb58Y'
        transfer=TransferData(access_token)
    file_from=input("Enter the file u want to transfer")
    file_to=input("Enter the path to which u want to transfer")
    transfer.upload_file(file_from,file_to)
    print("Your file has been moved")

    
    

main()

