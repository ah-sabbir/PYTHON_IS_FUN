import os
import time
if not (os.path.isfile("INPT_FOLDER_NAME.txt")):
    open("INPT_FOLDER_NAME.txt","w")
    
file=open("INPT_FOLDER_NAME.txt","r")
folder_names=[]
for line in file.readlines():
    folder_names.append(line)
file.close()

p=r"C:\\Users\\USER\\Desktop\\folder_maker"

if folder_names==[]:
    print("there is no Folder name you have entered or text file is emplty ")
    time.sleep(2)
else:
    for i in folder_names:
        m=i.replace("\n","")
        k=m.replace("'","")
        l=k.replace(":","")
        j=l.replace("?","")
        os.makedirs(os.path.join(p,j.replace('"'," ")))
    print("file has created")
    time.sleep(1)

