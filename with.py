with open ("codingal.txt","w") as f :
    f.write  ("HELLO EARTH")
f.close()



with open ("codingal.txt","r") as file :
    data = file.readlines()
    for line in data:
        word=line.split 
        print(word)
file.close()
    
    
    
    
    
    
    
file1 = open('new_document.txt','x') 




import os 
if os.path.exists("demofile.txt"):
    print("File exists !!!")
else:
    print("the file does not exist !!!")
    
    
    
file2 = open('new_document.txt','w') 



import os 
os.remove("new_document")


import os 
os.rmdir("Sample folder")