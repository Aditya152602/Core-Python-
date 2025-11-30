def name(fname,mname="Jhon",lname="Whatson"):
     print("Hello,", fname,mname,lname)
name("Amy")

def name (fname,mname,lname):
     print("Hello,",fname,mname,lname)
name(mname="Peter",lname="Wesker",fname="Jode")

def name(fname,mname,lname):
     print("Hello,",fname,mname,lname)
name("Peter","Quill")
def name (**name):
     print("Hello,",name["fname"],name["mname"],name["lname"])
     name(mname="ADITYA",lname="ANUJ",fname="DWIVEDI")

def name(fname,mname,lname):
     return "Hello,"+ fname+"  "+mname+"  "+lname
     print(name("Aditya", "Dhar","Dwivedi"))
