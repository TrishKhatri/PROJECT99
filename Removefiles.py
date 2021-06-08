import shutil as s
import os 
import time 




def Main():
    deletedfolders = 0
    deletedfiles = 0
    path = "/users/trish/desktop/WhatsApp"
    days = 5
    seconds = time.time() - (days*24*60*60)
    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            if seconds >= GetFileAge(root_folder):
                RemoveFolder(root_folder)
                deletedfolders += 1 
                break
            else:
                for folder in folders:
                    folderpath = os.path.join(root_folder,folder)
                    if seconds>= GetFileAge(folderpath):
                        RemoveFolder(folderpath)
                        deletedfolders +=1
                for file in files:
                    filepath = os.path.join(root_folder,file)
                    if seconds>= GetFileAge(filepath):
                        RemoveFiles(filepath)
                        deletedfiles +=1
            else:
                #If path is not a folder
                if seconds >= GetFileAge(path):
                    RemoveFiles(path)
                    deletedfiles+=1
    else:
        #File/Folder is not found
        print("Path not found")
        print(deletedfiles)
        print(deletedfolders)




def RemoveFiles(path):
    if not os.remove(path):
        print(f"{path} is removed successfully ")
    else:
        print("Unable to delete")



def RemoveFolder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed successfully ")
    else:
        print("Unable to delete")



def GetFileAge(path):
    seetime = os.stat(path).st_ctime
    return seetime

Main()


