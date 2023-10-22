############################################################## Developed and Copyright By Pavan Kumar S   #############################################################################

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
from cv2 import cv2
import os
import numpy as np
import csv 
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System") 
        self.root.wm_iconbitmap("face.ico")


        #=============== variables =================

        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()



        #img 1
        img = Image.open(r"img\smart-attendance.jpg")
        img = img.resize((800,200),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        #img 2
        img1 = Image.open(r"img\clg.jpg")
        img1 = img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200) 


        #background image
        img3 = Image.open(r"img\dev.jpg")
        img3 = img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="red",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #main frame
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left  label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=1,width=730,height=590)

        img_left = Image.open(r"img\girl.jpeg")
        img_left = img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label( Left_frame,image = self.photoimg_left)
        f_lbl.place(x=5,y=0,width=715,height=130)


        #main frame
        left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=135,width=715,height=430)

        Back_button=Button(title_lbl,text='Back',command=self.root.destroy,font=("arial",14,"bold"),width=13,bg="red",fg="white")
        Back_button.grid(row=1,column=2,padx=5,sticky=W)



        #Label Entry


            #Atendance id
        attendanceId_label = Label(left_inside_frame, text="Attendance Id:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10, pady=5, sticky=W )

        attendanceID_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10, pady=5, sticky=W)

            #roll
        roll_label = Label(left_inside_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10, pady=5, sticky=W )

        roll_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("times new roman",12,"bold"))
        roll_entry.grid(row=0,column=3,padx=10, pady=5, sticky=W)

            #name
        name_label = Label(left_inside_frame, text="Name:",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10, pady=5, sticky=W )

        name_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("times new roman",12,"bold"))
        name_entry.grid(row=1,column=1,padx=10, pady=5, sticky=W)

            #deparnment
        dep_label = Label(left_inside_frame, text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10, pady=5, sticky=W )

        dep_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=20,font=("times new roman",12,"bold"))
        dep_entry.grid(row=1,column=3,padx=10, pady=5, sticky=W)

            #time
        time_label = Label(left_inside_frame, text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10, pady=5, sticky=W )

        time_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",12,"bold"))
        time_entry.grid(row=2,column=1,padx=10, pady=5, sticky=W)

            #date
        date_label = Label(left_inside_frame, text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10, pady=5, sticky=W )

        date_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=3,padx=10, pady=5, sticky=W)

            #attendace
        attendance_label = Label(left_inside_frame, text="Attendance Status",font=("times new roman",12,"bold"),bg="white")
        attendance_label.grid(row=3,column=0,padx=10, sticky=W )

        self.atten_status = ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance ,font=("times new roman",12,"bold"),state="readonly",width=20)
        self.atten_status["values"] = ("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,padx=2,pady=10,sticky=W) 
        self.atten_status.current(0)  


         #buttons frame
        btn_frame = Frame(left_inside_frame ,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=350,width=715,height=35)

        import_btn = Button(btn_frame, text="Import csv",command=self.importCsv,font=("times new roman",12,"bold"),bg="blue",fg="white",width=19)
        import_btn.grid(row=0,column=0)

        export_btn = Button(btn_frame, text="Export csv",command=self.exportCsv,font=("times new roman",12,"bold"),bg="blue",fg="white",width=19)
        export_btn.grid(row=0,column=1)

        update_btn = Button(btn_frame, text="Update",command=self.action,font=("times new roman",12,"bold"),bg="blue",fg="white",width=19)
        update_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,command=self.reset_data ,text="Reset",font=("times new roman",12,"bold"),bg="blue",fg="white",width=19)
        reset_btn.grid(row=0,column=3)



        #right  label frame
        table_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE, text="Attendance Details",font=("times new roman",12,"bold"))
        table_frame.place(x=750,y=1,width=720,height=590)

        table_frame = Frame(table_frame ,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=705,height=530)


        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.AtendanceReportTable = ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AtendanceReportTable.xview)
        scroll_y.config(command=self.AtendanceReportTable.yview)


        self.AtendanceReportTable.heading("id",text="Id")
        self.AtendanceReportTable.heading("roll",text="Roll")
        self.AtendanceReportTable.heading("name",text="Name")
        self.AtendanceReportTable.heading("department",text="Department")
        self.AtendanceReportTable.heading("time",text="Time")
        self.AtendanceReportTable.heading("date",text="Date")
        self.AtendanceReportTable.heading("attendance",text="Attendance")
        self.AtendanceReportTable["show"] = "headings"

        self.AtendanceReportTable.column("id",width=100)
        self.AtendanceReportTable.column("roll",width=100)
        self.AtendanceReportTable.column("name",width=100)
        self.AtendanceReportTable.column("department",width=100)
        self.AtendanceReportTable.column("time",width=100)
        self.AtendanceReportTable.column("date",width=100)
        self.AtendanceReportTable.column("attendance",width=100)

        self.AtendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AtendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #=============fetch data============
    def fetchData(self, rows):
        self.AtendanceReportTable.delete(*self.AtendanceReportTable.get_children())
        for i in rows:
            self.AtendanceReportTable.insert("",END,values=i) 
    
    #===========import csv==============
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd,title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    
    #==============export csv============
    def exportCsv(self):
        try:
            if len(mydata) <1:
                messagebox.showerror("Error","No data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd,title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","your data exported to "+os.path.basename(fln)+"successfully",parent=self.root)
        except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    def search_data(self):
        if self.serchTxt_var.get()=="" or self.serch_var.get()=="Select Option":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='password',database='my_table')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where " +str(self.serch_var.get())+" LIKE '%"+str(self.serchTxt_var.get())+"%'")
                rows=my_cursor.fetchall()         
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # export upadte
    def action(self):
        id=self.var_atten_id.get()
        roll=self.var_atten_roll.get()
        name=self.var_atten_name.get()
        dep=self.var_atten_dep.get()
        time=self.var_atten_time.get()
        date=self.var_atten_date.get()
        attendn=self.var_atten_attendance.get()

        # write to csv file
        try:
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="a",newline="\n") as f:
                dict_writer=csv.DictWriter(f,fieldnames=(["ID","Roll","Name","Department","Time","Date","Attendance"]))
                dict_writer.writeheader()
                dict_writer.writerow({
                "ID":id,
                "Roll":roll,
                "Name":name,
                "Department":dep,
                "Time":time,
                "Date":date,
                "Attendance":attendn 
                    })
            messagebox.showinfo("Data Exported","Your data exported to " +os.path.basename(fln)+ " Successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)            
            

    def get_cursor(self, event=""):
        cursor_row = self.AtendanceReportTable.focus()
        content = self.AtendanceReportTable.item(cursor_row)

        row = content["values"] 

        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1]) 
        self.var_atten_name.set(row[2]) 
        self.var_atten_dep.set(row[3]) 
        self.var_atten_time.set(row[4]) 
        self.var_atten_date.set(row[5])
        self.var_atten_attendance.set(row[6]) 
             
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("") 
        self.var_atten_name.set("") 
        self.var_atten_dep.set("") 
        self.var_atten_time.set("") 
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")   

   


if __name__ == "__main__":
    root = Tk() 
    obj = Attendance(root)
    root.mainloop()