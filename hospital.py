
import imghdr
from pickle import FRAME
import mysql.connector
from string import whitespace
from tkinter import *
from PIL import Image,ImageTk
from appoint import AppointButton

class HospitalMangement:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Mangement")
        self.root.geometry("1550x800+0+0")


        #image
        img = Image.open(r"D:\big_data\hotel_mangemnet\hospitalslogan.jpg")
        img1=img.resize((1000,600),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)       
        label1=Label(self.root,image = self.photoimg1)
        label1.place(x=0,y=10,width=1000,height=800)

        #image2
        img11 = Image.open(r"D:\big_data\hotel_mangemnet\head.PNG")
        img2=img11.resize((1370,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)       
        label1=Label(self.root,image = self.photoimg2)
        label1.place(x=0,y=0,width=1370,height=150)
         

        #add apointment button
        btn_frame=Frame(bd=1,relief=RIDGE)
        btn_frame.place(x=990,y=105,width=230,height=30)

        add_btn=Button(btn_frame,text="BOOK APPOINTMENT",command=self.appoint_details,width=20,font=("times new roman",14,"bold"),bg="black",fg="white",bd=1,cursor="hand2")
        add_btn.grid(row=0,column=0)

        #doctors button
        btn_frame2=Frame(bd=1,relief=RIDGE)
        btn_frame2.place(x=840,y=105,width=130,height=30)

        add_btn1=Button(btn_frame2,text="Doctors",width=15,font=("times new roman",13,"bold"),bg="white",fg="black",bd=1,cursor="hand2")
        add_btn1.grid(row=0,column=0)
        
        #our departmentsbtn
        btn_frame3=Frame(bd=1,relief=RIDGE)
        btn_frame3.place(x=610,y=105,width=200,height=30)

        add_btn2=Button(btn_frame3,text="Our Departements",width=15,font=("times new roman",16,"bold"),bg="white",fg="black",bd=0,cursor="hand2")
        add_btn2.grid(row=0,column=0)

#for adding form window in appointment tab
    def appoint_details(self):
        self.new_window=Toplevel(self.root)
        self.app=AppointButton(self.new_window)

    


if __name__ == '__main__':
    root=Tk()
    obj=HospitalMangement(root)
    root.mainloop()