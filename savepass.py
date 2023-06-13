import os
def savepass(password,path,appname):
    filepath = os.path.join(path, 'passwords')
    if not os.path.exists(path):
       os.makedirs(path) 
    with open(filepath, "a") as f:
        f.write(password + ' (' + appname + ')')
        f.write("\n")