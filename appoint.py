import email
import imghdr
import mysql.connector
import random
from pickle import FRAME
from string import whitespace
from tkinter import messagebox, ttk 
from tkinter import *
from turtle import width
from tkcalendar import Calendar, DateEntry
from PIL import Image,ImageTk

class AppointButton:
    def __init__(self,root):
        self.root=root
        self.root.title("Book Appointmnet")
        self.root.geometry("600x475+400+80")
##################################33
        self.var_patientno=StringVar()
        x=random.randint(1,1000)
        self.var_patientno.set(str(x))

        self.var_firstname=StringVar()
        self.var_lastname=StringVar()
        self.var_email=StringVar()
        self.var_mobno=StringVar()
        self.var_doctorlist=StringVar()
        self.var_date=StringVar()

        #doctor appointment
        title=Label(self.root,text="Doctor Appointment",font=("times new roman",30,"bold"),bg="blue",fg="black")
        title.place(x=0,y=0,width=600,height=90)

        #please provide details
        #title2=Label(self.root,text="Please Fill Above Details:",font=("times new roman",10,"bold"))
        #title2.place(x=16,y=100,width=140,height=20)

        lbl_patientno=Label(self.root,text="Patient No",font=("arial",12,"bold"))
        lbl_patientno.place(x=10,y=100,width=120,height=20)

        patient_entry=ttk.Entry(self.root,textvariable=self.var_patientno,font=("times new roman",13,"bold"),state="readonly",width=25)
        patient_entry.place(x=146,y=100)



        lbl_first_name=Label(self.root,text="First Name",font=("arial",12,"bold"))
        lbl_first_name.place(x=0,y=150,width=140,height=20)
        
        first_entry=ttk.Entry(self.root,textvariable=self.var_firstname,font=("times new roman",13,"bold"),width=25)
        first_entry.place(x=150,y=150)

        lbl_last_name1=Label(self.root,text="Last Name",font=("arial",12,"bold"))
        lbl_last_name1.place(x=16,y=200)
  
        lbl_last_name1=ttk.Entry(self.root,textvariable=self.var_lastname,font=("times new roman",13,"bold"),width=25)
        lbl_last_name1.place(x=146,y=200)

        mob_no=Label(self.root,text="Mobile Number",font=("arial",12,"bold"))
        mob_no.place(x=16,y=250)
        mob_no=ttk.Entry(self.root,textvariable=self.var_mobno,font=("times new roman",13,"bold"),width=25)
        mob_no.place(x=146,y=250)

        email=Label(self.root,text="Email",font=("arial",12,"bold"))
        email.place(x=16,y=300)
        email=ttk.Entry(self.root,textvariable=self.var_email,font=("times new roman",13,"bold"),width=25)
        email.place(x=146,y=300)

        doctors_list=Label(self.root,text="Doctors List",font=("arial",12,"bold"))
        doctors_list.place(x=16,y=350)

        self.doctor_combo=ttk.Combobox(self.root,textvariable=self.var_doctorlist,font=("times new roman",13),justify=CENTER,state="readonly",width=23)
        self.doctor_combo["values"]=("Select Doctor Name","Dr.Rajesh Patil(MS(GEneral Surgery),FNB(MAS))","Dr.Pradeep Makkar(M.S.OBS & Gynae)","Dr.Ramesh Dhiman(MD Medicine)","Dr.Vasant Naik(DM Nephrology)","Dr.Dhiraj Patil(M.D Pediatrics)","Dr.Jay Sagar(M.S Ortho)")
        self.doctor_combo.place(x=146,y=350)
        self.doctor_combo.current(0)
        #radio_doc1=Radiobutton(value="Dr.Rajesh Patil",font=("times new roman",15))
        #radio_doc1.place(x=146,y=350)

        date_select=Label(self.root,text="Select Date",font=("arial",12,"bold"))
        date_select.place(x=16,y=400)

        cal = DateEntry(self.root, width= 16,textvariable=self.var_date,background= "magenta3", foreground= "white",bd=2)
        cal.place(x=146,y=400)
        


        self.submit2 = Button(self.root,text="Submit", command=self.add_data,font="aried 12 bold",width=12, height=1, bg='lightgreen')
        self.submit2.place(x=20, y=430)
   
    def add_data(self):
        if self.var_firstname.get()=="" or self.var_lastname.get()=="":
            messagebox.showerror("Please Fill All Fields") 
        else:
            try:
            

                conn=mysql.connector.connect(host="localhost",username="root",password="harsh@123",database="hospital_management")
                
                my_cursor=conn.cursor()
                add_datas=("""insert into appointment(`patient_no`,`first_name`,`last_name`,`mob_no`,`email`,`choosen_doctor`,`appointment_date`)values(%s,%s,%s,%s,%s,%s,%s)""")
                data_user=(self.var_patientno.get(),self.var_firstname.get(),self.var_lastname.get(),self.var_mobno.get(),self.var_email.get(),
                        self.var_doctorlist.get(),self.var_date.get())
                my_cursor.execute(add_datas,data_user)                      
                messagebox.showinfo("sucesss")
                conn.commit()
            except Exception as es:
                messagebox.showwarning("warning",f"some thing went wrong:{str(es)}")

if __name__ == '__main__':
    root=Tk()
    obj=AppointButton(root)
    root.mainloop()