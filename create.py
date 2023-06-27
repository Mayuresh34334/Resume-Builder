from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def login_page():
    signup_window.destroy()
    import login



class Login():
    def __init__(self,signup_window):
        self.signup_window = signup_window
        self.signup_window.title('Resume Generator')
        #self.signup_window.geometry('1500x1000+50+50')
        self.signup_window.state('zoomed')
        self.signup_window.resizable(True,True)

        self.bg=ImageTk.PhotoImage(file = 'image.png')
        self.bg_image = Label(self.signup_window , image=self.bg)
        self.bg_image.pack()

    


        #====Login Frame
        Frame_Login = Frame(self.signup_window, bg = 'white')
        Frame_Login.place(x=550,y=170, height=500, width =500 ) 

        title = Label(Frame_Login,text = 'Create Account', font =('Impact',35,'bold'),fg = '#d77337',bg='white')
        title.place(x=90,y=30)

        desc = Label(Frame_Login, text='Create',font=("Goudy old style",15,'bold'),fg='#d25d17',bg='white')
        desc.place(x=90,y=100)

        lbl_user = Label(Frame_Login, text='Enter Username',font=("Goudy old style",15,'bold'),fg='gray',bg='white')
        lbl_user.place(x=90,y=140)

        self.txt_user=Entry(Frame_Login, font=('Times New Roman',15),bg='lightgray')
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_email = Label(Frame_Login, text='Enter Email id',font=("Goudy old style",15,'bold'),fg='gray',bg='white')
        lbl_email.place(x=90,y=210)

        self.txt_email=Entry(Frame_Login, font=('Times New Roman',15),bg='lightgray')
        self.txt_email.place(x=90,y=240,width=350,height=35)

        lbl_pass = Label(Frame_Login, text='Enter Password',font=("Goudy old style",15,'bold'),fg='gray',bg='white')
        lbl_pass.place(x=90,y=280)

        self.txt_pass=Entry(Frame_Login, font=('Times New Roman',15),bg='lightgray')
        self.txt_pass.place(x=90,y=310,width=350,height=35)

        lbl_cpass = Label(Frame_Login, text='Confirm Password',font=("Goudy old style",15,'bold'),fg='gray',bg='white')
        lbl_cpass.place(x=90,y=350)

        self.txt_cpass=Entry(Frame_Login, font=('Times New Roman',15),bg='lightgray')
        self.txt_cpass.place(x=90,y=380,width=350,height=35)

        goto = Button(Frame_Login , text ='Go to login',command = login_page,cursor='hand2',bd=0,font = ('Times New Roman',12),bg='white',fg='#d77337')
        goto.place(x=200,y=450)
        

        login_btn = Button(self.signup_window ,command = self.login_function,cursor='hand2',  text ='Create',font = ('Times New Roman',20),fg='white',bg='#d77337')
        login_btn.place(x=700,y=650,width=180,height=40)

        self.var1 = IntVar()
        Checkbutton(Frame_Login,bd=0, text="all terms and conditions agreed",bg='white',fg='#d77337',font=('Times New Roman',15), variable=self.var1).place(x=110,y=420)

    def clear(self):
        self.txt_user.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_pass.delete(0,END)
        self.txt_cpass.delete(0,END)
    
    def login_function(self):
        if self.txt_email.get() == ' ' or self.txt_user.get() == ' ' or self.txt_pass.get() == "" or self.txt_user.get()=="":
            messagebox.showerror('Error','All fields are required',parent = self.signup_window)
        elif self.txt_pass.get() != self.txt_cpass.get():
            messagebox.showerror('Error','Password mismatched',parent = self.signup_window)
        elif self.var1.get() == 0:
            messagebox.showwarning('Warning','Tick the checkbox',parent = self.signup_window)
        else:
            try:
                con = pymysql.connect(host='localhost' , user='root',port = 3306, password='Na@9119553127')
                mycursor = con.cursor()
            except:
                messagebox.showerror('Error','Database Connectivity Issue,Please Try Again')
                return

            try:
                query = 'create database userdata'
                mycursor.execute(query)
                query = 'use userdata'
                mycursor.execute(query)
                query = 'create table data(id int auto_increment primary key not null, username varchar(50), email varchar(100),password varchar(20))'
                mycursor.execute(query)
            except:
                mycursor.execute('use userdata') 
            query = 'select * from data where username=%s'
            mycursor.execute(query,(self.txt_user.get()))
            row = mycursor.fetchone()
            if row != None:
                messagebox.showerror('Error','Username already exist')
            else:
                query = 'insert into data(username,email,password) value(%s,%s,%s)' 
                mycursor.execute(query,(self.txt_user.get(),self.txt_email.get(),self.txt_pass.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Registration is successful')
                #clear()
                signup_window.destroy()
                import login
            
 
    

signup_window = Tk()
obj = Login(signup_window)
signup_window.mainloop()