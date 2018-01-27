
import os
import zipfile
#enter working directory here
os.chdir('./Desktop/auto_vpn')
dir_name = os.getcwd().split('\\')[len(os.getcwd().split('\\'))-1]
#we are creating a zip file whose name is same as that of the directory, it can be changed to whatever..
ziphandle=zipfile.ZipFile(dir_name+'.zip', 'w', zipfile.ZIP_DEFLATED)
for root, dirs, files in os.walk(os.getcwd()):
    for file in files: 
        f=os.path.join(root, file)
        if file==dir_name+'.zip' : continue
        ziphandle.write(f)
        print(str(f)+' added')
ziphandle.close()
