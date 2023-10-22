############################################################## Developed and Copyright By Pavan Kumar S   #############################################################################

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from main import Face_Recognition_System


def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()



class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.root.wm_iconbitmap("face.ico")

        #img 1
        img = Image.open(r"img\BestFacialRecognition.jpg")
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #img 2
        img1 = Image.open(r"img\university.jpg")
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130) 

        #img 3
        img2 = Image.open(r"img\images.jpg")
        img2 = img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image = self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #background image
        img3 = Image.open(r"img\img1.jpeg")
        img3 = img3.resize((1530,750),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl = Label(bg_img, text="FACIAL RECOGNITION ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        downtitle=Label(self.root,text="Note:Enter Valid Username and Password",font=("times new roman",25,"bold"),bg="white",fg="darkblue")
        downtitle.place(x=0,y=755,width=1600,height=35)

        title_lbl = Label(text="DEVELOPER - PAVAN", font=("times new roman",13,"bold"),fg="black")
        title_lbl.place(x=5,y=765,width=180,height=20)


        
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=200,width=340,height=430)

        img9=Image.open(r"img\My_eQuals_Homepage_Students_Icon_Red.jpg")
        img9=img9.resize((90,90),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        lblimg9=Label(image=self.photoimg9,bg="black",borderwidth=0)
        lblimg9.place(x=730,y=200,width=90,height=90)


        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=85)

        username_lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=150)

        self.txtuser=StringVar()
        self.txtpass=StringVar()

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,show='*',font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)



        img2=Image.open(r"img\images1.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=355,width=25,height=25)

        img3=Image.open(r"img\editlock.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=425,width=25,height=25)

        loginbtn=Button(frame, text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        
        registerbtn=Button(frame, text="NEW USER REGISTER",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        
        forgetbtn=Button(frame, text="FORGET PASSWORD",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=15,y=370,width=160)

        
        Back_button=Button(frame,text='Back',command=self.root.destroy,font=("arial",11,"bold"),width=5,bg="red",fg="white")
        Back_button.place(x=200,y=390,width=100)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    
 

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required")
        elif self.txtuser.get()=="Pavan" and self.txtpass.get()=="password":
            messagebox.showinfo("Success","Welcome to Pavan Project") 
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="password",database="my_table")
            my_cursor=conn.cursor() 
            my_cursor.execute("Select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()

                                                                                        ))   

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Authority Person")
                if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=Face_Recognition_System(self.new_window)  
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
 

    

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select" or self.txt_security.get()=="" or self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter the new Password",parent=self.root2)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="password",database="my_table")
                my_cursor=conn.cursor() 
                query=("Select * from register where email=%s and securityQ=%s and securityA=%s")
                value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone() 
                if row==None:
                 messagebox.showerror("Error","Please Enter Correct Answer",parent=self.root2) 
                else:
                    query=("update register set password=%s where email=%s")
                    value=(self.txt_newpass.get(),self.txtuser.get())
                    my_cursor.execute(query,value)

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Info","Your Password has been reset,Please login with New Password",parent=self.root2)
                    self.root2.destroy()
                    self.txtuser.focus()

            except Exception as es:
                messagebox.showerror("Error",f"Error Due to :(str(es))",parent=self.root2)        
                   

                         
                 

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="password",database="my_table")
            my_cursor=conn.cursor() 
            query=("Select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("My Error","Please Enter the valid user name",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170") 

                l=Label(self.root2,text="FORGET PASSWORD",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)  

                
                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),fg="black",bg="white")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your College Name","Your Teacher Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),fg="black",bg="white")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)

               
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")


        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        


        self.bg=ImageTk.PhotoImage(file=r"img\di.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        self.bg1=ImageTk.PhotoImage(file=r"img\550-5505432_registration-registration-png-transparent-png.png")
        bg_lbl=Label(self.root,image=self.bg1)
        bg_lbl.place(x=50,y=100,width=470,height=550)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)


        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)


        
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="black",bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="black",bg="white")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your College Name","Your Teacher Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)


        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        pswd.place(x=50,y=310)

        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

        img=Image.open(r"img\77-772557_register-button-png-photos-register-here-button-png.png")
        img=img.resize((200,55),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=10,y=420,width=200)


        img1=Image.open(r"img\depositphotos_1982796-stock-illustration-login-icon-button.jpg")
        img1=img1.resize((200,45),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=330,y=420,width=200)



    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & Confirm password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and Condition",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="password",database="my_table")
            my_cursor=conn.cursor() 
            query=("Select * from register where email=%s")
            value=(self.var_email.get(),) 
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email",parent=self.root)
            else:
                my_cursor.execute("Insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                           self.var_fname.get(),
                                                                                           self.var_lname.get(),
                                                                                           self.var_contact.get(),
                                                                                           self.var_email.get(),
                                                                                           self.var_securityQ.get(),
                                                                                           self.var_securityA.get(),
                                                                                           self.var_pass.get()
                                                                                
                                                                                       )) 
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully",parent=self.root)      


    def return_login(self):
        self.root.destroy()                                                                        


                                                                                                         

if __name__ == "__main__":
    main()


    



            