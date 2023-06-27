from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql



def create_page():
    root.destroy()
    import create

def reset_page():
    root.destroy()
    import reset

def generate():
    root.destroy()
    import n1


class Login():
    def __init__(self,root):
        self.root = root
        self.root.title('Resume Generator')
        #self.root.geometry('1500x1000+50+50')
        self.root.state('zoomed')
        self.root.resizable(True,True)

        self.bg=ImageTk.PhotoImage(file = 'image.png')
        self.bg_image = Label(self.root , image=self.bg)

        self.bg_image.pack()



        #====Login Frame
        Frame_Login = Frame(self.root, bg = 'white')
        Frame_Login.place(x=550,y=270, height=340, width =500 ) 

        title = Label(Frame_Login,text = 'Login Here', font =('Impact',35,'bold'),fg = '#d77337',bg='white')
        title.place(x=90,y=30)

        desc = Label(Frame_Login, text='User login',font=("Goudy old style",15,'bold'),fg='#d25d17',bg='white')
        desc.place(x=90,y=100)

        lbl_user = Label(Frame_Login, text='Username',font=("Goudy old style",15,'bold'),fg='gray',bg='white')
        lbl_user.place(x=90,y=140)
        

        self.txt_user=Entry(Frame_Login, font=('Times New Roman',15),bg='lightgray')
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_pass = Label(Frame_Login, text='Password',font=("Goudy old style",15,'bold'),fg='gray',bg='white')
        lbl_pass.place(x=90,y=210)

        self.txt_pass=Entry(Frame_Login, font=('Times New Roman',15),bg='lightgray')
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        forget = Button(Frame_Login , text ='Forget Password ?',command = reset_page,cursor='hand2',bd=0,font = ('Times New Roman',12),bg='white',fg='#d77337')
        forget.place(x=90,y=280)

        create = Button(Frame_Login , text ='Create Account',command = create_page,cursor='hand2',bd=0,font = ('Times New Roman',13),bg='white',fg='#d77337')
        create.place(x=300,y=280)

        login_btn = Button(self.root , command = self.login_function,cursor='hand2',  text ='Login',font = ('Times New Roman',20),fg='white',bg='#d77337')
        login_btn.place(x=700,y=590,width=180,height=40)


    def login_function(self):
        if self.txt_pass.get() == "" or self.txt_user.get()=="":
            messagebox.showerror('Error','All fields are required',parent = self.root)
        else:
            try:
                con=pymysql.connect(host='localhost',user = 'root', port = 3306, password='Na@9119553127')
                mycursor = con.cursor()
            except:
                messagebox.showerror('Error','Connection is not established try again')
                return
            query = 'use userdata'
            mycursor.execute(query)
            query = 'SELECT * FROM data WHERE username=%s AND password=%s'
            username = self.txt_user.get()
            password = self.txt_pass.get()
            mycursor.execute(query, (username, password))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error','Invalid username or password')
            else:
                messagebox.showinfo('Welcome','Login is successful')
                command = generate()

root = Tk()
obj = Login(root)
root.mainloop()