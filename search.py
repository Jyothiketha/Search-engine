from drives import *
from multithreading import *

def individual(query,filename):
    global flag
    for d in query:
        drv=d+":\\"
        for root,dirs,files in os.walk(drv):
            for name in files:
                if name==filename:
                    result=(str(os.path.join(root,name)))
                    print(result)
                    flag=1
    return(flag)
d=mydrive()
query=input("enter the drive u want to search in:")
filename=input("enter the filename:")
flag=individual(query,filename)
if flag==0:
    print("file not found:")

