############################################################## Developed and Copyright By Pavan Kumar S   #############################################################################


from tkinter import * 
from tkinter import ttk
import tkinter 
from PIL import Image, ImageTk
from student import Student
from train import Train
from attendance import Attendance
from developer import Developer
from face_recognition import Face_Recognition
from time import strftime
from datetime import datetime
import os
from chatbot import Chatbot


class Face_Recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
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
        img3 = Image.open(r"img\k3Vh6xZ.jpg")
        img3 = img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)



        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font = ('times new roman',14,'bold'),background = 'white',foreground = 'blue')
        lbl.place(x=0,y=0,width=110,height=50)  
        time()  





        #student button
        img4 = Image.open(r"img\student.jpg")
        img4 = img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image = self.photoimg4, command=self.student_details ,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details ,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


        #detect face button
        img5 = Image.open(r"img\face_detector1.jpg")
        img5 = img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image = self.photoimg5,command=self.face_date, cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_date,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)


         #attendance button
        img6 = Image.open(r"img\smart-attendance.jpg")
        img6 = img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image = self.photoimg6, command=self.attendance_date, cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_date,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        #train button
        img8 = Image.open(r"img\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img8 = img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image = self.photoimg8, command=self.train_data,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)

        b1_1 = Button(bg_img, text="Train Face", cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)


        #photos button
        img9 = Image.open(r"img\pic1.jpg")
        img9 = img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image = self.photoimg9, command=self.open_img,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)


        #developer button
        img10 = Image.open(r"img\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img10 = img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img,command=self.developer_date ,image = self.photoimg10, cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1 = Button(bg_img,command=self.developer_date, text="Developer", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)


        #exit button
        img11 = Image.open(r"img\exit.jpg")
        img11 = img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img,command=self.iExit, image = self.photoimg11, cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1 = Button(bg_img,command=self.iExit ,text="Exit", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)

        #chat button
        img_chat = Image.open(r"img\robot-icon-bot-sign-design-2785674.jpg")
        img_chat = img_chat.resize((220,220),Image.ANTIALIAS)
        self.photoimg_chat = ImageTk.PhotoImage(img_chat)

        bChat = Button(bg_img,command=self.chatbot, image = self.photoimg_chat, cursor="hand2")
        bChat.place(x=1100,y=100,width=220,height=220)

        b1_Chat = Button(bg_img,command=self.chatbot ,text="ChatBot", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_Chat.place(x=1100,y=300,width=220,height=40)


        # ======== functions buttons ==========


    def open_img(self):
        os.startfile("data")

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_date(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_date(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_date(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def chatbot(self):
        self.new_window=Toplevel(self.root)
        self.app=Chatbot(self.new_window)   



    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure exit this project?",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return
    

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop( )