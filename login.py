import json,re
print("* * * hello welcome to login sign up page * * *")
loginsignup=input("loginsignup::")
if True:
    if loginsignup=="signup":
        a=open("ishu.json","r")
        c=a.read()
        data=json.loads(c)
        # obj1=open("student.txt","w")
        # obj1.close()
        username=input("enter the first name and last name:-")
        surname=input("enter the surname:-")
        phone=str(input("enter the phone no:-"))
        if len(phone)==10:
                dop=input("enter the DOB:-")
                gender=input("enter the gender:-")
                if gender=="male" or gender=="female":
                    password=input("enter the password:-")
                    if re.search(r'[0-9,A-Z,a-z,@#$!]',password):
                        print("strong password")
                        conform_password=input("enter the password:")
                        username={"username":username,"surname":surname,"password":password,"phone":phone,"gender":gender,"dop":dop}
                        data.update(username)
                        if password==conform_password:
                            print("***signup succefully***")
                            with open("ishika.json","a")as fh:
                                b=json.dump(data,fh,indent=2)
                        else:
                            print("invalide password")
                    else:
                        print("wrong password")
                else:
                    print("your gender is wrong")
        else:
            print("your mobile number is wrong")
    elif loginsignup=="login":
        username=input("enter the username")