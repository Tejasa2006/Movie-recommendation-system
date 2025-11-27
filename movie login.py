import tkinter as tk 
import tkinter
import sqlite3
import random
from tkinter import messagebox as ms
from PIL import Image,ImageTk
from tkinter.ttk import *

root=tk.Tk()
root.configure(background='white')

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))
root.title("login")

image2=Image.open('img1.png')
image2=image2.resize((w,h),Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root,image=background_image)
background_label.image = background_image
background_label.place(x=0,y=0)

#############################################################################################################


Email = tk.StringVar()
password = tk.StringVar() 
 
def login():
 

    with sqlite3.connect('movie.db') as db:
         c = db.cursor()

        
         db = sqlite3.connect('movie.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS DataReg"
                        "(name TEXT, address TEXT,  Email TEXT, country TEXT, Phoneno TEXT, Gender TEXT, password TEXT)")
         db.commit()
         
         
         find_entry = ('SELECT * FROM DataReg WHERE Email = ? and password = ?')
         
         c.execute(find_entry, [(Email.get()), (password.get())])
         result = c.fetchall()
         if result:
            msg = ""
          
            print(msg)
            ms.showinfo("messege", "Login sucessfully")
            

            from subprocess import call
            call(['python','GUI_Master.py'])
            
           
         
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')


a11=tk. Label(root,text='Login Here ',fg='white',bg ='black',font=('Forte',25)).place(x=700,y=200)

canvas1=tk.Canvas(root,background="black",highlightbackground="red")
canvas1.place(x=560,y=250,width=450,height=350)

#login=Label(root,text="Login",font=('Arial',25),foreground='green').place(x=270,y=350)
a11=tk. Label(root,text='Enter Email',bg='black',fg="white",font=('Cambria',15)).place(x=600,y=305)
a12=tk. Label(root,text='Enter Password',bg='black',fg="white",font=('Cambria',15)).place(x=600,y=355)

b11=tk.Entry(root,width=40, textvariable=Email).place(x=750,y=310,)
b12=tk. Entry(root,width=40,show='*', textvariable=password).place(x=750,y=360,)


def forgot():
    from subprocess import call
    call(['python','movie forgot password.py'])


button2=tk.Button(root,text="Forgot Password?",fg='black',bg='#27ae60',command=forgot)
button2.place(x=850,y=430)



button2=tk.Button(root,text="Log in",font=("Bold",9),command=login,width=50,bg='#2980b9')
button2.place(x=610,y=500)

a=tk. Label(root,text='Not a Member?',font=('Cambria',11),bg='black',fg="white").place(x=800,y=550)

def reg():
    from subprocess import call
    call(['python','movie registration.py'])

button1=tk.Button(root,text="sign up",fg='black',bg='#27ae60',command=reg)
button1.place(x=915,y=550,width=55)



root.mainloop()