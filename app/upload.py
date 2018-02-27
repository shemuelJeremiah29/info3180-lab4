import os

    rootdir = os.getcwd()
    print rootdir 

def get_uploaded_images(): 
    lst=[] 
    
    for subdir, dirs, files in os.walk(rootdir + '/app/static/upload'):
        for file in files:
            lst[file]+=os.path.join(subdir, file) 
    
    return lst