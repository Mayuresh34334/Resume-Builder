from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def login_page():
    reset_window.destroy()
    import login



class Login():
    def __init__(self,reset_window):
        self.reset_window = reset_window
        self.reset_window.title('Resume Generator')
        #self.reset_window.geometry('1500x844+50+50')
        self.reset_window.state('zoomed')
        self.reset_window.resizable(True,True)

        self.bg=ImageTk.PhotoImage(file = 'reset.png')
        self.bg_image = Label(self.reset_window , image=self.bg)
        self.bg_image.pack()


        #====Login Frame
        Frame_Login = Frame(self.reset_window, bg = 'white')
        Frame_Login.place(x=930,y=210, height=420, width =500 ) 

        title = Label(Frame_Login,text = 'Reset Password', font =('Impact',35,'bold'),fg = '#f8d3c7',bg='white')
        title.place(x=90,y=30)

        desc = Label(Frame_Login, text='Set password',font=("Goudy old style",15,'bold'),fg='#fe9b9f',bg='white')
        desc.place(x=90,y=100)

        lbl_user = Label(Frame_Login, text='Username',font=("Goudy old style",15,'bold'),fg='gray',bg='white')
        lbl_user.place(x=90,y=140)

        self.txt_user=Entry(Frame_Login, font=('Times New Roman',15),bg='lightgray')
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_pass = Label(Frame_Login, text='Password',font=("Goudy old style",15,'bold'),fg='gray',bg='white')
        lbl_pass.place(x=90,y=210)

        self.txt_pass=Entry(Frame_Login, font=('Times New Roman',15),bg='lightgray')
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        lbl_cpass = Label(Frame_Login, text='Confirm password',font=("Goudy old style",15,'bold'),fg='gray',bg='white')
        lbl_cpass.place(x=90,y=280)

        self.txt_cpass=Entry(Frame_Login, font=('Times New Roman',15),bg='lightgray')
        self.txt_cpass.place(x=90,y=310,width=350,height=35)

        goto = Button(Frame_Login , text ='Go to login',command = login_page,cursor='hand2',bd=0,font = ('Times New Roman',12),bg='white',fg='#d77337')
        goto.place(x=90,y=350)

        

        login_btn = Button(self.reset_window , command = self.login_function,cursor='hand2',  text ='Reset',font = ('Times New Roman',20),fg='black',bg='#f8d3c7')
        login_btn.place(x=1080,y=610,width=180,height=40)

    def login_function(self):
        if self.txt_user.get() == '' or self.txt_pass.get() == "" or self.txt_user.get()=="":
            messagebox.showerror('Error','All fields are required',parent = self.reset_window)
        elif self.txt_pass.get() != self.txt_cpass.get():
            messagebox.showerror('Error','Password mismatched',parent = self.reset_window) 
        else:
            try:
                con=pymysql.connect(host='localhost',user = 'root', port = 3306, password='Na@9119553127')
                mycursor = con.cursor()
            except:
                messagebox.showerror('Error','Connection is not established try again',parent = self.reset_window)
                return
            query = 'use userdata'
            mycursor.execute(query)
            query = 'SELECT * FROM data WHERE username = %s'
            username = self.txt_user.get()
            mycursor.execute(query, (username,))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error','Username not found')
            else:
                query = 'update data set password = %s where username = %s' 
                mycursor.execute(query,(self.txt_pass.get(),self.txt_user.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset',parent = self.reset_window)
                reset_window.destroy()
                import login
                


reset_window = Tk()
obj = Login(reset_window)
reset_window.mainloop()