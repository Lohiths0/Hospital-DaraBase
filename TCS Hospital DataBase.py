import os
class Admin:
  
  def __init__(self):
        self.name=""
        self.title=""
        self.gender=""
        self.dob=""
        self.qual=""
        self.med_lic_no=""
        self.teresa_scan_cen_id=""
        self.add=""
        self.contact=""
        self.email=""
        self.l=[]
        
  def getDocData(self):
    
        """Stores all the data entered in a list which is later writen into a file"""
    
        self.count+=1 #counts the number of records
        def title():
            titles=["Radiologist","Cardiologist","Pathologist"]
            for i in range(len(titles)):
                print (str(i+1)+" "+titles[i])
            print ("Choose from above")
            print ("Enter 4 for adding new title")
            choice=int(input("Enter choice:"))
            if choice==1:
                return "Radiologist"
            elif choice==2:
                return "Cardiologist"
            elif choice==3:
                return "Pathologist"
            elif choice==4:
                new_title=input("Enter new title:")
                titles.append(new_title.capitalize())
                return new_title.capitalize()
        self.name=input("Enter doctor's name:")#0
        self.title=title()#1
        self.gen=input("Enter gender:")#2
        self.dob=input("Enter date of birth dd/mm/yy:")#3
        self.qual=input("Enter doctor's qualification:")#4
        self.med_lic_no=input("Enter Medical License Number:")#5
        self.tere_scan_cen_id=input("Enter Teresa Scan Center Id:")#6
        self.add=input("Enter doctor's address:")#7
        self.contact=input("Enter doctor's number:")#8
        self.email=input("Enter doctor's email id:")#9
       
        self.l.append(self.name)#0
        self.l.append(self.title)#1
        self.l.append(self.gen)#2
        self.l.append(self.dob)#3
        self.l.append(self.qual)#4
        self.l.append(self.med_lic_no)#5
        self.l.append(self.tere_scan_cen_id)#6
        self.l.append(self.add)#7
        self.l.append(self.contact)#8
        self.l.append(self.email)#9
  

  def name_search(self):
      """Searches for name from a file"""
      """Retrives data line by line and stores in list"""
      
      doc=open("doc.txt","r")
      name=input("Enter name to be searched:")
      records=[]
      for i in doc:
          records.append(i.split("-"))
      number=len(records)
      for j in range(number):
          if records[j][0]==name:
              doc.close()
              return records[j]


  def contactnum_search(self):
    """Searches for contact number from a file"""
    """Retrives data line by line and stores in list"""
    doc=open("doc.txt","r")
    number=input("Enter contact number to be searched:")
    records=[]
    for i in doc:
        rec=i.split("-")
        if rec[8]==number:
          return rec


  




  def Teresascanid_search(self):
    """Searches for teresa scan center id from a file"""
    """Retrives data line by line and stores in list"""
    doc=open("doc.txt","r")
    TSC_id=input("Enter Teresa Scan Center Id to be searched:")
    records=[]
    for i in doc:
        records.append(i.split("-"))
    number=len(records)
    for j in range(number):
        if records[j][6]==TSC_id:
            doc.close()
            return records[j]


  def medlic_search(self):
    """Searches for medical license number from a file"""
    """Retrives data line by line and stores in list"""
    doc=open("doc.txt","r")
    med_lic=input("Enter medical licence to be searched:")
    records=[]
    for i in doc:
        records.append(i.split("-"))
    number=len(records)
    for j in range(number):
        if records[j][5]==med_lic:
            doc.close()
            return records[j]


  


  def modify_details(self):
    """Used to modify details"""
    
    """Retrives data line by line and stores in list"""
    """Modifies data using list indices and later joins the list to make a string which is later written onto a file"""
    #0-name
    #1-title
    #2-gender
    #3-dob
    #4-qualification
    #5-medical license no
    #6-teresa scan id
    #7-address
    #8-number
    #9-email
    doc=open("doc.txt","r")
    new=open("newdoc.txt","a")
    print ("1.Name")
    print ("2.Title")
    print ("3.Gender")
    print ("4.Date Of Birth")
    print ("5.Qualification")
    print ("6.Medical license no")
    print ("7.Teresa scan id")
    print ("8.Address")
    print ("9.Number")
    print ("10.Email")
    choice=int(input("Enter choice of record:"))
    existing_name=input("Enter name of whose info you want to change:")
    new_record=input("Enter new record:")
    index=choice-1
  
    if choice==10:
      new_record+="\n"
      
    check=True
    for i in doc:
      rec_list=i.split("-")
      print (rec_list)
      
      if rec_list[0]==existing_name:
        rec_list[index]=new_record
        print (rec_list)
        str_rec_list="-".join(rec_list)
        new.write(str_rec_list)
        print (str_rec_list)
        new.flush()
        
        check=False
      else:
        new.write(i)
        new.flush()
    if check==True:
        print ("Record not there in data")
    else:
        print ("Updated")
    
    os.remove("doc.txt")
    os.rename("newdoc.txt","doc.txt")
    



class doctors():
  def __init__(self):
        self.regnum=""
        self.regdate=""
        self.name=""
        self.gen=""
        self.dob=""
        self.add=""
        self.contnum=""
        self.refer=""
        self.test_date=""
        self.test_type=""
        self.docname=""
        self.fee=""
        self.l=[]
        self.count=0


  def getPatData(self):
        """"Stores all the data entered in a list which is later writen into a file"""
        self.count+=1 #counts the number of records
        def test_type():
            tests=["X-ray","ECG","CT Scan","MRI Scan","Cardiac CT"]
            for i in range(len(tests)):
                print (str(i+1)+" "+titles[i])
            print ("Choose from above")
            print ("Enter 6 for adding new title")
            choice=int(input("Enter choice:"))
            if choice==1:
                return tests[0]
            elif choice==2:
                return tests[1]
            elif choice==3:
                return tests[2]
            elif choice==4:
              return tests[3]
            elif choice==5:
              return tests[4]
            elif choice==6:
              new_test=input("Enter new title:")
              tests.append(new_title.capitalize())
              return new_test.capitalize()
        self.regnum=input("Enter Registration number:")#0
        self.regdate=input("Enter Registration date:")#1
        self.name=input("Enter Name:")#2
        self.gen=input("Enter Patient's gender:")#3
        self.dob=input("Enter Date Of Birth  of patient dd/mm/yy:")#4
        self.add=input("Enter Patient's address:")#5
        self.contnum=input("Enter Patient's contact number:")#6
        self.refer=input("Hospital was refered by:")#7
        self.test_date=input("Enter Test date:")#8
        self.docname=input("Enter Doctor name:")#9
        self.fee=input("Fee(in rs):")#10
        
        
        self.l.append(self.regnum)#0
        self.l.append(self.regdate)#1
        self.l.append(self.name)#2
        self.l.append(self.gen)#3
        self.l.append(self.dob)#4
        self.l.append(self.add)#5
        self.l.append(self.contnum)#6
        self.l.append(self.refer)#7
        self.l.append(self.test_date)#8
        self.l.append(self.docname)#9
        self.l.append(self.fee)#10
  def registrationnum_Search(self):
      """Searches for registration number from a file"""
      """Retrives data line by line and stores in list"""
      pat=open("pat.txt","r")
      regnum=input("Enter patient's registration num to be searched:")
      records=[]
      for i in pat:
        records.append(i.split("-"))
        number=len(records)
      for j in range(number):
        if records[j][0]==regnum:
          pat.close()
          return records[j]

  def patientname_Search(self):
      """Searches for patient name from a file"""
      """Retrives data line by line and stores in list"""
      pat=open("pat.txt","r")
      name=input("Enter patient's name to be searched:")
      records=[]
      for i in pat:
          
          records.append(i.split("-"))
      
      number=len(records)
      for j in range(number):
          if records[j][2]==name:
              pat.close()
              return records[j]

  def contactnum_Search(self):
      """Searches for contact number from a file"""
      """Retrives data line by line and stores in list"""
      pat=open("pat.txt","r")
      num=input("Enter patient's contact num to be searched:")
      records=[]
      for i in pat:
          records.append(i.split("-"))
      number=len(records)
      for j in range(number):
          if records[j][6]==num:
              pat.close()
              return records[j]


  def modify_pat_details(self):
    """Used to modify details"""
    
    """Retrives data line by line and stores in list"""
    """Modifies data using list indices and later joins the list to make a string which is later written onto a file"""
    #0-registration number
    #1-registration date
    #2-name
    #3-gender
    #4-dob
    #5-add
    #6-contact number
    #7-reference
    #8-test date
    #9-doctor name
    #10-fee
    doc=open("pat.txt","r")
    new=open("newpat.txt","a")
    print ("1.Registration number")
    print ("2.Registration date")
    print ("3.Name")
    print ("4.Gender")
    print( "5.Date of Birth")
    print ("6.Address")
    print ("7.Contact Number")
    print ("8.Reference")
    print ("9.Test Date")
    print ("10.Change Doctor")
    print ("11.Fee")
    choice=int(input("Enter choice of record:"))
    existing_rec=input("Enter Patient's Registration number:")
    new_record=input("Enter new record:")
    index=choice-1
    if index==10:
      new_record+="\n"
      
      
    check=True
    for i in doc:
      rec_list=i.split("-")
      if rec_list[0]==existing_rec:        
        rec_list[index]=new_record 
        str_rec_list="-".join(rec_list)
        new.write(str_rec_list)
        new.flush()
        check=False
      else:
        new.write(i)
        new.flush()

    if check==True:
      print ("Record not there in data")
    else:
      print ("Updated")
        
    
    os.remove("pat.txt")
    os.rename("newpat.txt","pat.txt")
    

def admin_login():
  ad=Admin()
  print ("1.Add doctor")
  print ("2.Search Name of doctor")
  print ("3.Search Contact Number of doctor")
  print ("4.Search Medical License Number of doctor")
  print ("5.Search Teresa Scan Center Id of doctor")
  print ("6.Modify Details")
  choice=int(input("Enter choice:"))
  if choice==1:
    doc_list=open("doc.txt","a")
    ad.getDocData()
    rec=ad.l
    str_rec="-".join(rec)
    doc_list.write(str_rec)
    doc_list.write("\n")
    doc_list.close()
  elif choice==2:
    print (ad.name_search())
  elif choice==3:
    print (ad.contactnum_search())
  elif choice==4:
    print (ad.medlic_search())
  elif choice==5:
    print (ad.Teresascanid_search())
  elif choice==6:
    print (ad.modify_details()
    )

  
def doc_login():
  doc=doctors()
  print ("1.Add patient")
  print ("2.Search registration number")
  print ("3.Search patient namme")
  print ("4.Search phone number")
  print ("5.Modify any details")
  choice= int(input("Enter choice:"))
  if choice==1:
    pat_list=open("pat.txt","a")
    doc.getPatData()
    rec=doc.l
    str_rec="-".join(rec)
    pat_list.write(str_rec)
    pat_list.write("\n")
    pat_list.close()
  elif choice==2:
    print (doc.registrationnum_Search())
    
  elif choice==3:
    print (doc.patientname_Search())
  elif choice==4:
    print (doc.contactnum_Search())
  elif choice==5:
    doc.modify_pat_details()
  else:
    print( "invalid entry")
    
#--------------------------------    
admin_password=[""]
doc_password=[""]
#--------------------------------

c = True

def sys_login(passw,mode):
    if mode==1:
        global admin_password
        if passw in admin_password:
            return True
        else:
            return False
    if mode==2:
        global doc_password
        if passw in doc_password:
            return True
        else:
            return False




c=True
while c:
  print ("1.Login")
  print ("2.Signup")
  print ("3.Quit")
  ch=int(input("Enter choice:"))
  if ch==3:
    print ("Ok thanks")
    c=False
  elif ch==2:
    print ("1.Signup as admin")
    print ("2.Signup as doctor")
    wish=int(input("Enter choice:"))
    if wish==2:
      new_pass=input("Enter new password:")
      doc_password.append(new_pass)
      print ("Added")
    elif wish==1:
      new_pass=input("Enter new password:")
      admin_password.append(new_pass)
      print  ("Added")
  elif ch==1:
    print ("1.Login as admin")
    print ("2.Login as doctor")
    e=int(input("Enter choice:"))
    p=input("Enter password:")
    if e==1:
      if p in admin_password:
        print ("login successful!!!")
        h=True
        while h:
          admin_login()
          g=input("Enter 'No' to stop or hit Enter to continue:")
          if g.lower()=="no":
            print ("Ok thanks")
            h=False
          
      else:
        print ("Incorrect password")

    elif e==2:
      if p in doc_password:
        print ("login successfull!!!"
        )
        h=True
        while h:
          doc_login()
          g=input("Enter 'No' to stop or hit Enter to continue:")
          if g.lower()=="no":
            print ("Ok thanks")
            h=False

