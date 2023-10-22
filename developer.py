############################################################## Developed and Copyright By Pavan Kumar S   #############################################################################

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from cv2 import cv2

class Developer:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System") 
        self.root.wm_iconbitmap("face.ico") 

        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open(r"img\dev.jpg")
        img_top = img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label( self.root,image = self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        #main frame
        main_frame = Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=500 )

        dev_img = Image.open(r"img\photo_1.jpg")
        dev_img = dev_img.resize((200,200),Image.ANTIALIAS)
        self.photo_dev_img = ImageTk.PhotoImage(dev_img)

        f_lbl_img = Label( main_frame,image = self.photo_dev_img)
        f_lbl_img.place(x=300,y=0,width=200,height=200)

        #developer info
        dev_label = Label(main_frame, text="Hello my name is S Pavan Kumar",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label = Label(main_frame, text="I am a developer of this face recognition",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        dev_label = Label(main_frame, text="contact me on pavanpvnpavan20@gmail.com",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=0,y=70)

        dev_img_inside = Image.open(r"img\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        dev_img_inside = dev_img_inside.resize((500,300),Image.ANTIALIAS)
        self.photo_dev_img_inside = ImageTk.PhotoImage(dev_img_inside)

        f_lbl_img = Label( main_frame,image = self.photo_dev_img_inside)
        f_lbl_img.place(x=0,y=210,width=500,height=300)

         
        Back_button=Button(title_lbl,text='Back',command=self.root.destroy,font=("arial",11,"bold"),width=13,bg="red",fg="white")
        Back_button.grid(row=1,column=2,padx=5,sticky=W)







if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()