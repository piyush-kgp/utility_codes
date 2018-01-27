
import os
import zipfile
#enter working directory here
os.chdir('./Desktop/auto_vpn')
dir_name = os.getcwd().split('\\')[len(os.getcwd().split('\\'))-1]
a=zipfile.ZipFile(dir_name+'.zip', 'w', zipfile.ZIP_DEFLATED)
for root, dirs, files in os.walk(os.getcwd()):
    for file in files: 
        f=os.path.join(root, file)
        a.write(f)
        print(str(f)+' added')
a.close()
