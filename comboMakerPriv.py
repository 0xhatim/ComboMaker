'''

    Programed By Mexaw Alotebi 
    Not Allowed For Stealing 
    Public Soruce Not For Sale 
    @31421
    
'''
try:
    import os
    import sys
    import concurrent.futures
    import autopy 
    import time 
except Exception as e:
    print(e)
    

    install = ["autopy"]
    for i in install:
        msg = "pip install "+ i
        os.system(msg)
        input(":")
        sys.exit()
    



print('''
    1 - For one Target Added To Combo ! 
    2 - Normal Added ..  
    3 - username + userame (123 - 123456 123user123
''')
qa = int(input(":"))
try:

    usernamelist = open("username.txt","r").read().splitlines()
    passwordlist = open("password.txt","r").read().splitlines()
except Exception as r:
    print("Please Make Sure u Had ,",r)

def comboMaker(user,password):

    with open("comboSave.txt","a") as wr:

        wr.write(user+":"+password+"\n")
        wr.write(i+":"+"123"+password+"123"+"\n")

 # Loop in All user name with thread Each user #  
 # i is single user ! 
 # 
if qa == 1:

    i  = str(input("input your username Target:"))  
def comboMakerPassword(password):

    try:
        with open("comboSave.txt","a") as wr:
            wr.write(i+":"+password+"\n")
    except Exception as e:

        print(e)

start = time.process_time()

try:

    if qa == 3:
       
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            Mexaw_Alotebi = {executor.submit(comboMaker,user,user): user for user in usernamelist}

    elif len(password_list) >=500 and qa==1:
        with concurrent.futures.ThreadPoolExecutor(max_workers=400) as executor:
            
            Mexaw_Alotebi = {executor.submit(comboMakerPassword,password): password for password in passwordlist}
    elif len(password) <=500:
        for i in usernamelist:
            for m in passwordlist:
                comboMaker(i,m)

    else:
        for i in usernamelist:
            for m in passwordlist:
                comboMaker(i,m)


except Exception as e:
    print(e)
time = time.process_time() - start
autopy.alert.alert("Time Taken :{}".format(time),"Message From Mexaw Combo ")


input("")