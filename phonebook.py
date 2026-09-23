import sys 
def initial_phonebook():
    rows , cols = int(input("pls enter initial amount of number of contacts")),5
    
    
    
    
    
    phone_book=[]
    print(phone_book)
    for i in range (rows):
        print("/nEnter contact %d details in the following order(ONLY):"%(i+1))
        print("NOTE : * indicates mandotary fields")
        print("...")
        temp=[]
        for j in range (cols):
            if j==0:
                temp.append(str(input("Enter your name *:")))
                if temp[j] == '' or temp[j] == '' :
                    sys.exit(
                        "Name is manditory field.Process exiting due to blank field"
                    )
                    if j==1:
                        temp.append(str(input("Enter Number *:")))
                        
                    if j==2:
                        temp.append(str(input("Enter E-mail address:")))  
                        if temp[j] == '' or temp[j] == '' :
                            temp[j] = None
                        
                              
                      
                        