############################################################## Developed and Copyright By Pavan Kumar S   #############################################################################

from tkinter import * 
from tkinter import ttk
from PIL import Image, ImageTk


class Chatbot:
    def __init__(self, root):
        self.root=root
        self.root.geometry("730x620+0+0")
        self.root.title("ChatBot")
        self.root.bind('<Return>',self.enter_func)
        self.root.wm_iconbitmap("face.ico")



        main_frame=Frame(self.root,bd=4,bg='blue',width=610)
        main_frame.pack()

        img_chat = Image.open(r"img\robot-icon-bot-sign-design-2785674.jpg")
        img_chat = img_chat.resize((200,70),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        title_label = Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text="CHAT ME", font=("arial",30,"bold"),bg="white",fg="green")
        title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()


        label_1=Label(btn_frame,text="Type Something",font=("arial",14,"bold"),bg="white",fg="green")
        label_1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',15,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send>>",command=self.send,width=8,font=('arial',15,'bold'),bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,text="Clear Data",command=self.clear,width=8,font=('arial',14,'bold'),bg='red',fg='white')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)


        self.msg=''
        self.label_11=Label(btn_frame,text=self.msg,font=("arial",14,"bold"),bg="white",fg="green")
        self.label_11.grid(row=1,column=1,padx=5,sticky=W)

        Back_button=Button(btn_frame,text='Back',command=self.root.destroy,font=("arial",13,"bold"),width=8,bg="red",fg="white")
        Back_button.grid(row=1,column=2,padx=5,sticky=W)
                              


    def enter_func(self,event):
        self.send.invoke()

    def clear(self):
        self.text.delete('1.0',END) 
        self.entry.set('')   
          

    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send) 

        if (self.entry.get()==''):
            self.msg='Please Enter Some Input'
            self.label_11.config(text=self.msg,fg='red')
        else:
            self.msg=''
            self.label_11.config(text=self.msg,fg='red') 

        if (self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot: Hii')

        elif (self.entry.get()=="hii"):
            self.text.insert(END,"\n\n"+"Bot: Hello")

        elif (self.entry.get()=="how are you"):
            self.text.insert(END,"\n\n"+"Bot: I am Fine What about you")

        elif (self.entry.get()=="good"):
            self.text.insert(END,"\n\n"+"Bot: Nice To Hear")

        elif (self.entry.get()=="who created you"):
            self.text.insert(END,"\n\n"+"Bot: S.Pavan Kumar Using Python") 

        elif (self.entry.get()=="Difference Between Artificial Intelligence And Machine Learning"):
            self.text.insert(END,"\n\n"+"Bot: Artificial intelligence is a technology which enables a machine to simulate human behavior Machine learning is a subset of AI which allows a machine to automatically learn from past data without programming explicitly. The goal of AI is to make a smart computer system like humans to solve complex problems.")
   
        elif (self.entry.get()=="what are the key features of Python"):
            self.text.insert(END,"\n\n"+"Bot: Easy to code. Python is a high-level programming language.Free and Open Source.Object-Oriented Language.GUI Programming Support.High-Level Language.Extensible feature.Python is Portable language.Python is Integrated language")

        elif (self.entry.get()=="what is your name"):
            self.text.insert(END,"\n\n"+"Bot: My Name is Mr.ROBO 2.0 Named by Pavan") 

        elif (self.entry.get()=="project team members"):
            self.text.insert(END,"\n\n"+"Bot: Pavan , Ranjitha , Tejaswini")

        elif (self.entry.get()=="who is a father of AI "):
            self.text.insert(END,"\n\n"+"Bot: Alan Turing")  

        elif (self.entry.get()=="what is Visual Studio Code"):
            self.text.insert(END,"\n\n"+"Bot: Visual Studio Code is a source-code editor made by Microsoft for Windows, Linux and macOS. Features include support for debugging, syntax highlighting, intelligent code completion, snippets, code refactoring, and embedded Git.")     

        elif (self.entry.get()=="what is MySQL"):
            self.text.insert(END,"\n\n"+"Bot: MySQL is an open source relational database management system. Its name is a combination of “My”, the name of co-founder Michael widenius’s daughter ,and “SQL” , the abbreviation for Structured Query Language.")      

        elif (self.entry.get()=="How to create a student database in Excel"):
            self.text.insert(END,"\n\n"+"Bot: Step 1: Entering the data. ...Step 2: Entering Data Correctly. ...Step 3: Know that the Rows are called Records. ...Step 4: Know that the Columns are called Fields. ...Step 5: Creating the Table. ...Step 6: Using the Database Tools. ...Step 7: Expanding the Database. ...Step 8: Completing the Database Formatting.")    

        elif (self.entry.get()=="can you speak kannada"):
            self.text.insert(END,"\n\n"+"Bot: I'm still Learning it....")  

        elif (self.entry.get()=="what is Machine Learning"):
            self.text.insert(END,"\n\n"+"Bot: Machine Learning is an AI technique getting significant attention today.The ultimate aim of machine learning is to enable software applications to become more accurate without being explicitly  programmed.")

        elif (self.entry.get()=="what is AI"):
            self.text.insert(END,"\n\n"+"Bot: Artificial Intelligence is the ability of machine like computer to perform  function that normally require human intelligence.")   

        elif (self.entry.get()=="what Are The Applications Of Face Recognition"):
            self.text.insert(END,"\n\n"+"Bot: •Prevent Retail Crime,•Unlock Phones.•Smarter Advertising.•Find Missing Persons.•Help the Blind.•Protect Law Enforcement.•Aid Forensic Investigations.•Identify People on Social Media Platforms…...")  

        elif (self.entry.get()=="How many countries use Facial Recognition"):
            self.text.insert(END,"\n\n"+"Bot: China ,U.S, New york…")  

        elif (self.entry.get()=="who invented Facial Recognition"):
            self.text.insert(END,"\n\n"+"Bot: Woody Bledsoe")  

        elif (self.entry.get()=="How To Face Recognition Step By Step"):
            self.text.insert(END,"\n\n"+"Bot: Step 1: Face detection. The camera detects and locates the image of a face, either alone or in a crowd. ...Step 2: Face analysis. Next, an image of the face is captured and analyzed. ...Step 3: Converting the image to data. ...Step 4: Finding a match.")            

        elif (self.entry.get()=="what is Python"):
            self.text.insert(END,"\n\n"+"Bot: Python is a general purpose , high level interpreted language with easy syntax and dynamic semantics Created by Guido Van Rossum in 1989.")  

        elif (self.entry.get()=="what is chatbot"):
            self.text.insert(END,"\n\n"+"Bot: ChatterBot is a Python library that is designed to deliver automated responses to user inputs. It makes use of a combination of ML algorithms to generate many different types of responses.")  

        elif (self.entry.get()=="bye"):
            self.text.insert(END,"\n\n"+"Bot: Thank you For Chatting")

        else:
            self.text.insert(END,"\n\n"+"Bot: Sorry I didn't get it")                
                                        









if __name__ == "__main__":
    root = Tk()
    obj = Chatbot(root)
    root.mainloop( )        